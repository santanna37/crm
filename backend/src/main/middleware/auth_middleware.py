import os 
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from pathlib import Path
from src.presentation.http_types.status_code import HTTPStatus
from dotenv import load_dotenv
import requests
import base64
import json

# Isso garante que as variáveis carreguem assim que o arquivo for lido
env_path = Path(__file__).parent.parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

security = HTTPBearer(auto_error=False)

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://lipajeykqlitxzooxjza.supabase.co")
SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")

# Cache da chave pública do Supabase
_supabase_public_key = None

def get_supabase_public_key():
    """
    Busca a chave pública do Supabase via JWKS e converte para PEM.
    O Supabase novo usa ES256 (ECDSA P-256).
    """
    global _supabase_public_key

    if _supabase_public_key is not None:
        return _supabase_public_key

    try:
        jwks_url = f"{SUPABASE_URL}/auth/v1/.well-known/jwks.json"
        response = requests.get(jwks_url, timeout=5)

        if response.status_code == 200:
            jwks = response.json()

            # Pega a primeira chave (ou a que corresponder ao kid)
            if "keys" in jwks and len(jwks["keys"]) > 0:
                key = jwks["keys"][0]

                # Converte JWK EC para PEM
                # JWK EC tem: x, y, crv (P-256)
                x = base64.urlsafe_b64decode(key["x"] + "==")
                y = base64.urlsafe_b64decode(key["y"] + "==")

                # Constrói a chave pública usando cryptography
                from cryptography.hazmat.primitives.asymmetric import ec
                from cryptography.hazmat.primitives import serialization

                # P-256 = secp256r1
                public_numbers = ec.EllipticCurvePublicNumbers(
                    int.from_bytes(x, 'big'),
                    int.from_bytes(y, 'big'),
                    ec.SECP256R1()
                )
                public_key = public_numbers.public_key()

                # Exporta como PEM
                pem = public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )

                _supabase_public_key = pem.decode('utf-8')
                print(f"[AUTH] Chave pública ES256 carregada com sucesso")
                return _supabase_public_key

        print(f"[AUTH] Falha ao buscar JWKS: {response.status_code}")
        return None

    except Exception as e:
        print(f"[AUTH] Erro ao buscar JWKS: {e}")
        return None

def verify_admin(credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    """
    Valida que a requisição tem um JWT válido de um usuário admin.
    Suporta ES256 (novo Supabase) e HS256 (legado).
    """

    # Sem token
    if credentials is None:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="falha no login - falta token",
            headers={"WWW-Authenticate": "Bearer"}
        )

    token = credentials.credentials

    # Lê o header do JWT para saber o algoritmo
    try:
        header = jwt.get_unverified_header(token)
        alg = header.get("alg", "HS256")
        kid = header.get("kid")
        print(f"[AUTH] Token alg={alg}, kid={kid}")
    except Exception as e:
        print(f"[AUTH] Erro ao ler header: {e}")
        alg = "HS256"

    payload = None

    # ESTRATÉGIA 1: ES256 (Supabase novo)
    if alg == "ES256":
        public_key_pem = get_supabase_public_key()

        if public_key_pem:
            try:
                payload = jwt.decode(
                    token,
                    public_key_pem,
                    algorithms=["ES256"],
                    audience="authenticated"
                )
                print(f"[AUTH] ✅ Token ES256 válido: {payload.get('email')}")
            except JWTError as e:
                print(f"[AUTH] ❌ Falha ES256: {e}")
        else:
            print("[AUTH] ⚠️ Chave pública não disponível, tentando fallback HS256")

    # ESTRATÉGIA 2: HS256 (legado / fallback)
    if payload is None and SUPABASE_JWT_SECRET:
        try:
            payload = jwt.decode(
                token,
                SUPABASE_JWT_SECRET,
                algorithms=["HS256"],
                audience="authenticated"
            )
            print(f"[AUTH] ✅ Token HS256 válido: {payload.get('email')}")
        except JWTError as e:
            print(f"[AUTH] ❌ Falha HS256: {e}")

    # Se nenhuma estratégia funcionou
    if payload is None:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Sessão invalida",
            headers={"WWW-Authenticate": "Bearer"}
        )

    # Verifica se é admin
    app_metadata = payload.get("app_metadata", {})
    user_role = app_metadata.get("role") or payload.get("role")

    print(f"[AUTH] Role detectada: {user_role}")
    print(f"[AUTH] App metadata: {app_metadata}")

    if user_role != "admin" and app_metadata.get("role") != "admin":
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Area de admin - role necessária: admin"
        )

    return payload
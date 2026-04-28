import os 
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from pathlib import Path
from src.presentation.http_types.status_code import HTTPStatus


# Isso garante que as variáveis carreguem assim que o arquivo for lido
env_path = Path(__file__).parent.parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
#print(os.environ)
# -----------------------------------


security = HTTPBearer(auto_error=False) # não retorna erro automatico 

SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")


def verify_admin(credentials:HTTPAuthorizationCredentials = Security(security)) -> dict:
    """
    Valida que a requisição tem um JWT válido de um usuário admin.
    
    Usado como Depends() nas rotas privadas.
    Rotas públicas NÃO usam essa função — não tem nem importado.
    """

    #sem token 
    if credentials is None:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail = "falha no login - falta token",
            headers = {"WWW-Authenticate": "Bearer"}
        )
    
    if not SUPABASE_JWT_SECRET:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail= "Configuração de auth ausente no servidor"
        )
    
    try:
        payload = jwt.decode(
            credentials.credentials,
            SUPABASE_JWT_SECRET,
            algorithms=["HS256"],
            audience="authenticated"
        )
    
    except JWTError:
        raise HTTPException(
            status_code= HTTPException.UNAUTHORIZED,
            detail = "Sessão inmvalida",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    app_metadata = payload.get("app_metadata",{})
    if app_metadata.get("role") !="admin":
        raise HTTPException(
            status_code= HTTPStatus.UNAUTHORIZED,
            detail = "Area de admin"
        )

    return payload 



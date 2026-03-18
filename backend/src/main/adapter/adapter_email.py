# adapter_email.py

# BIBLIOTECAS 
import os 
import base64
import re
from pathlib import Path
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart

# Bibliotecas da Brevo
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

# Garante o carregamento das variáveis de ambiente
env_path = Path(__file__).parent.parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


class AdapterEmail:

    def __init__(self):
        # Configuração da API Brevo
        self.configuration = sib_api_v3_sdk.Configuration()
        
        api_key = os.getenv("BREVO_API_KEY")
        if not api_key:
            raise ValueError("BREVO_API_KEY não encontrada no .env")
        
        self.configuration.api_key['api-key'] = api_key
        
        self.api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(self.configuration)
        )
        
        # ESSENCIAL: Definir o atributo _host
        self._host = os.getenv("EMAIL_HOST")
        if not self._host:
            raise ValueError("EMAIL_HOST não encontrado no .env")
        
        print(f"[DEBUG] AdapterEmail inicializado. Host: {self._host}")

    def send_email(self, email: str, email_class: MIMEMultipart, subject: str = None):
        html_content = ""
        inline_images = {}  # cid -> (base64, content_type)
        attachments = []
        
        # 1. Extrai partes do email
        for part in email_class.walk():
            content_type = part.get_content_type()
            content_id = part.get("Content-ID", "").strip("<>")
            
            # Pega o HTML
            if content_type == "text/html":
                html_content = part.get_payload(decode=True).decode("utf-8")
                continue
            
            # Pega imagens e anexos
            payload = part.get_payload(decode=True)
            if not payload:
                continue
            
            # Converte para base64 limpo
            b64 = base64.b64encode(payload).decode("utf-8").replace("\n", "").replace("\r", "")
            filename = part.get_filename() or "imagem.png"
            
            # Se tem Content-ID, é imagem inline
            if content_id:
                inline_images[content_id] = (b64, content_type)
                # Também adiciona como anexo (opcional, para compatibilidade)
                attachments.append({"content": b64, "name": filename})
            else:
                # Anexo normal
                attachments.append({"content": b64, "name": filename})
        
        # 2. SUBSTITUI CID POR DATA URI (ESSENCIAL!)
        for cid, (b64_data, mime_type) in inline_images.items():
            # Padrão regex para encontrar src="cid:..." ou src='cid:...'
            pattern = rf'src=["\']cid:{re.escape(cid)}["\']'
            # Data URI que funciona na Brevo
            data_uri = f"data:{mime_type};base64,{b64_data}"
            replacement = f'src="{data_uri}"'
            
            # Substitui no HTML
            html_content = re.sub(pattern, replacement, html_content)
            
            print(f"[DEBUG] Substituído cid:{cid} -> data:{mime_type};base64,...")
        
        # 3. Debug do HTML final (primeiros 500 chars)
        print(f"[DEBUG] HTML final (preview): {html_content[:500]}...")
        
        # 4. Monta o envio para Brevo
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{"email": email}],
            html_content=html_content,
            subject=subject or "Bem-vindo ao CRM!",
            sender={"name": "CRM Sant", "email": self._host},
            attachment=attachments if attachments else None
        )

        # No adapter, antes de enviar:
        html_size_kb = len(html_content.encode('utf-8')) / 1024
        print(f"[DEBUG] Tamanho do HTML: {html_size_kb:.2f} KB")

        # Se for maior que 1024KB (1MB), provavelmente será truncado
        if html_size_kb > 1024:
            print("⚠️ [AVISO] HTML muito grande! Imagem pode ser truncada.")
        
        try:
            response = self.api_instance.send_transac_email(send_smtp_email)
            print(f"✅ [BREVO] Email enviado: {response.message_id}")
            return True
        except ApiException as e:
            print(f"❌ [BREVO] API Error: {e}")
            return False
        except Exception as e:
            print(f"❌ [BREVO] Erro inesperado: {e}")
            return False
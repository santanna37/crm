from src.domain.use_case.case_email.use_case_email_interface import UseCaseEmailInterface
from email.mime.multipart import MIMEMultipart
from src.domain.models.model_person import PersonModel
from src.domain.constants.constant_email_send import TEMPLATE_WELCOME
from src.main.adapter.adapter_email import AdapterEmail
from typing import Dict

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

import os  # Adicione no topo

class UseCaseEmail(UseCaseEmailInterface):
    
    def __init__(self, adapter: AdapterEmail):
        self._adapter = adapter  

    def builder(self, email_class: Dict) -> MIMEMultipart:
        message = MIMEMultipart("related")
        
        # HTML body
        body = email_class.get("body", "")
        message.attach(MIMEText(body, "html", "utf-8"))
        
        # Processa imagens inline
        for img in email_class.get("images", []):
            path = img["path"]
            img_id = img["id"]
            img_type = img.get("type", "png")
            
            print(f"[DEBUG] Processando: {img_id} -> {path}")
            
            # Verifica se arquivo existe
            if not os.path.exists(path):
                raise FileNotFoundError(f"Imagem não encontrada: {path}")
            
            # Lê o arquivo de forma garantida
            try:
                with open(path, "rb") as f:
                    raw_bytes = f.read()
                
                print(f"[DEBUG] Lidos {len(raw_bytes)} bytes de {path}")
                
                if len(raw_bytes) < 100:
                    print(f"[WARNING] Arquivo muito pequeno! Conteúdo: {raw_bytes[:20]}")
                    continue  # Pula imagens inválidas
                
                # Cria MIMEImage
                mime_img = MIMEImage(raw_bytes)
                mime_img.add_header("Content-ID", f"<{img_id}>")
                mime_img.add_header("Content-Disposition", "inline")
                message.attach(mime_img)
                print(f"[DEBUG] Imagem {img_id} anexada com sucesso")
                
            except Exception as e:
                print(f"[ERROR] Falha ao processar {img_id}: {e}")
                raise
        
        # Processa anexos tradicionais
        for att in email_class.get("attachments", []):
            with open(att["path"], "rb") as f:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition", 
                    f'attachment; filename="{att.get("filename", "file")}"'
                )
                message.attach(part)
        
        return message

    def welcome_email(self, email: str, email_class: Dict):
        person_email = str(email)
        build_email = self.builder(email_class=email_class)
        send_email = self._adapter.send_email(email=person_email, email_class=build_email)
        return send_email
# use_case_email.py

from src.domain.use_case.case_email.use_case_email_interface import UseCaseEmailInterface
from src.main.adapter.adapter_email import AdapterEmail
from typing import Dict
import os


class UseCaseEmail(UseCaseEmailInterface):
    
    def __init__(self, adapter: AdapterEmail):
        self._adapter = adapter  

    def builder(self, email_class: Dict) -> Dict:
        """
        Builder simplificado - retorna dict puro, não MIME.
        A Brevo monta o email internamente.
        """
        result = {
            "subject": email_class.get("subject", "Campanha CLAUDINHO"),
            "html": email_class.get("body", ""),
            "images": [],
            "attachments": []
        }
        
        # Processa imagens inline (lê e valida apenas)
        for img in email_class.get("images", []):
            path = img["path"]
            img_id = img["id"]
            
            print(f"[DEBUG] Validando imagem: {img_id} -> {path}")
            
            if not os.path.exists(path):
                raise FileNotFoundError(f"Imagem não encontrada: {path}")
            
            file_size = os.path.getsize(path)
            print(f"[DEBUG] Imagem {img_id}: {file_size} bytes")
            
            result["images"].append({
                "id": img_id,
                "path": path,
                "type": img.get("type", "png")
            })
        
        # Processa anexos (só valida paths)
        for att in email_class.get("attachments", []):
            if not os.path.exists(att["path"]):
                raise FileNotFoundError(f"Anexo não encontrado: {att['path']}")
            result["attachments"].append(att)
        
        print(f"[DEBUG] Builder finalizado: {len(result['images'])} imagens, {len(result['attachments'])} anexos")
        return result

    def welcome_email(self, email: str, email_class: Dict):
        person_email = str(email)
        email_data = self.builder(email_class=email_class)
        send_email = self._adapter.send_email(
            email=person_email, 
            email_data=email_data  # Passa dict direto
        )
        return send_email
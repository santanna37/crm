# adapter_email.py

import os
import base64
from pathlib import Path
from dotenv import load_dotenv
from typing import Dict

from brevo_python import Configuration, ApiClient
from brevo_python.api import transactional_emails_api
from brevo_python.models import SendSmtpEmail, SendSmtpEmailInlineImage

# Carrega .env
env_path = Path(__file__).parent.parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


class AdapterEmail:

    def __init__(self):
        configuration = Configuration()
        configuration.api_key['api-key'] = os.getenv("BREVO_API_KEY")
        
        self.api_instance = transactional_emails_api.TransactionalEmailsApi(
            ApiClient(configuration)
        )
        
        self._host = os.getenv("EMAIL_HOST")
        print(f"[DEBUG] AdapterEmail inicializado (brevo-python). Host: {self._host}")

    def send_email(self, email: str, email_data: Dict):
        inline_images = []
        attachments = []

        # ✅ Processa imagens inline
        for img in email_data.get("images", []):
            with open(img["path"], "rb") as f:
                encoded = base64.b64encode(f.read()).decode("utf-8")

            inline_images.append(
                SendSmtpEmailInlineImage(
                    name=f"{img['id']}.{img.get('type', 'png')}",
                    content=encoded,
                    content_id=img["id"]  # snake_case na nova SDK também
                )
            )
            print(f"[DEBUG] Inline preparada: {img['id']} ({len(encoded)} chars)")

        # ✅ Processa anexos (se houver)
        for att in email_data.get("attachments", []):
            with open(att["path"], "rb") as f:
                encoded = base64.b64encode(f.read()).decode("utf-8")
            attachments.append({
                "name": att.get("filename", "arquivo"),
                "content": encoded
            })

        # Debug do HTML
        print("=" * 50)
        print("HTML ENVIADO:")
        print(email_data["html"])
        print("=" * 50)

        # ✅ Monta email com inline_images no construtor
        send_smtp_email = SendSmtpEmail(
            to=[{"email": email}],
            subject=email_data["subject"],
            html_content=email_data["html"],
            sender={"name": "CRM Sant", "email": self._host},
            inline_images=inline_images  # ✅ Funciona no construtor!
        )

        # Adiciona attachments se houver
        if attachments:
            send_smtp_email.attachment = attachments

        # ✅ Envia
        try:
            response = self.api_instance.send_transac_email(send_smtp_email)
            print(f"✅ [BREVO] Email enviado: {response.message_id}")
            return True
        except Exception as e:
            print(f"❌ [BREVO] Erro: {e}")
            import traceback
            traceback.print_exc()
            return False
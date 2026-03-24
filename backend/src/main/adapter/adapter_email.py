import os
import requests

class AdapterEmail:

    def __init__(self):
        self.api_key = os.getenv("BREVO_API_KEY")
        self._host = os.getenv("EMAIL_HOST")
        self.url = "https://api.brevo.com/v3/smtp/email"

    def send_email(self, email: str, email_data: dict):
        
        payload = {
            "sender": {
                "name": "CRM Sant",
                "email": self._host
            },
            "to": [{"email": email}],
            "subject": email_data["subject"],
            "htmlContent": email_data["html"] 
        }

        headers = {
            "accept": "application/json",
            "api-key": self.api_key,
            "content-type": "application/json"
        }

        print("=" * 60)
        print(f"🚀 Enviando e-mail (Link Externo) para: {email}")
        
        try:
            response = requests.post(self.url, json=payload, headers=headers)
            print("STATUS:", response.status_code)

            if response.status_code >= 400:
                print(f"❌ Erro na Brevo: {response.text}")
                return False

            print("✅ Sucesso! A imagem deve carregar via link da Wikipedia.")
            return True

        except Exception as e:
            print(f"❌ Erro de conexão: {e}")
            return False
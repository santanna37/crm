import os
import requests
import logging




logger = logging.getLogger(__name__)


class AdapterEmail:

    def __init__(self):
        self.api_key = os.getenv("BREVO_API_KEY")
        self._host = os.getenv("EMAIL_HOST")
        self.url = "https://api.brevo.com/v3/smtp/email"
        api_key = os.getenv("BREVO_API_KEY")
        print(f"[DEBUG] API Key carregada: {'SIM' if api_key else 'NÃO'}")
        print(f"[DEBUG] Primeiros 10 chars: {api_key[:10] if api_key else 'N/A'}...")
        logger.info(f"[DEBUG_BREVO] - API carregada: {'SIM' if api_key else 'NÃO'}")

    def send_email(self, email: str, email_data: dict):
        
        payload = {
            "sender": {
                "name": "Campanha CLAUDINHO",
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

    def get_email_info(self):
        """Busca estatísticas da conta para o Dashboard"""
        url_account = "https://api.brevo.com/v3/account"
        headers = {
            "accept": "application/json",
            "api-key": self.api_key
        }
        
        try:
            # Faz a requisição para pegar dados da conta
            response = requests.get(url_account, headers=headers, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                # Pegamos o e-mail da conta e o total de envios do mês
                return {
                    "status": "online",
                    "account_email": data.get("email", "n/a"),
                    "monthly_sent": data.get("statistics", {}).get("monthlyEmailSent", 0)
                }
            return {"status": "error", "msg": f"Status {response.status_code}"}
        except Exception as e:
            logger.error(f"Erro ao buscar info da Brevo: {e}")
            return {"status": "offline"}
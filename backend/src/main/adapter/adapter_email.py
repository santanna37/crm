# BIBLIOTECAS 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from dotenv import load_dotenv
import os 



# Isso garante que as variáveis carreguem assim que o arquivo for lido
env_path = Path(__file__).parent.parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
#print(os.environ)
# -----------------------------------


class AdapterEmail:

    def __init__(self):
        self._host = os.getenv("EMAIL_HOST")
        self._password = os.getenv("EMAIL_PASSWORD")
        self._port = int(os.getenv('EMAIL_PORT'))
        self._server = os.getenv("EMAIL_SERVER")
    

    def send_email(self ,email: str, email_class: MIMEMultipart):

        message = email_class
        message["From"] = self._host
        message["To"] = email
        
        try:
            with smtplib.SMTP(self._server, self._port, timeout=30) as server:
                server.starttls()
                server.login(self._host, self._password)
                server.send_message(message)
                return True
                # debug
        except Exception as exception:
            print(f"\nERRO REAL NO SMTP: {exception}") # Adicione isso!
            print(f"o erro foi {exception}")
            return False  


# BIBLIOTECAS 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
import os 

from src.domain.constants.constant_email_send   


# Isso garante que as variáveis carreguem assim que o arquivo for lido
env_path = Path(__file__).parent.parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
#print(os.environ)
# -----------------------------------


class AdapterEmail:

    def __init__(self):
        self._host = os.getenv("EMAIL_HOST")
        self._password = os.getenv("EMAIL_PASSWORD")
        self._port = os.getenv(EMAIL_PORT)
        self._server = os.getenv("EMAIL_SERVER")
    

    def send_email(email: str, email_class: MIMEMultipart):

        message = email_class
        message["From"] = self._host
        message["To"] = email
        message["Subject"] = email_class.get("Subject")
        message.attach(MIMEText,email_class.get("Body"))

        try:
            with smtplib.SMTP(self._server, self._port) as server:
                server.starttls()
                server.login(self._host, self._password)
                server.send_message(message)
                # debug
        except Exception as exception:
            return f"o erro foi {exception}"

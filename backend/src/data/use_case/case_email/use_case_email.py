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



class UseCaseEmail(UseCaseEmailInterface):
    
    def __init__(self, adapter: AdapterEmail):
        self._apapter = adapter  

    def buider(self, email_class: Dict):

        message = MIMEMultipart("related")
        
        body = email_class.get("body")
        if body:
            print("DEBUG-body: ",body)
            message.attach(MIMEText(body, "html", "utf-8"))
        
        image_body = email_class.get("image_body")
        if image_body:
            print('DEBUG-image-body :' ,image_body)
            path = image_body.get("path")
            
            with open(path,"rb") as img:
                img_body = MIMEImage(img.read())
                img_body.add_header("Content-ID",f"<{image_body.get("id")}>")
                message.attach(img_body)


        image_header = email_class.get("image_header")
        if image_header:
            print('DEBUG-image-header',image_header)
            path = image_header.get("path")

            with open(path,"rb") as anexo:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(anexo.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition",
                f'attachment; filename="imagem1.jpeg"')
                message.attach(part)
        
        return message

    def welcome_email(self, email:str, email_class:Dict):
        
        person_email = str(email)
        
        build_email = self.buider(email_class= email_class)

        send_email = self._apapter.send_email(email= person_email, email_class= build_email)

        return send_email
# BIBLIOTECAS 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

from src.domain.constants import constant_email_send


def buider(email_class:dict):

    message = MIMEMultipart("related")
    
    if email_class.body is not None:
        message.attach(MIMEText(email_class.body,"html"))
    
    if email_class.image is not None:
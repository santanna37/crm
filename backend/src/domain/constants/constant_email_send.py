import os 
from pathlib import Path

# 1. Pega o caminho absoluto de onde este arquivo (constant_email_send.py) está
current_dir = Path(__file__).parent.resolve()

# 2. Navega até a pasta 'media' de forma relativa ao arquivo atual
# Se o arquivo está em src/domain/constants/, a imagem está em media/
image_path = str(current_dir / "media" / "estrela_pt.png")

TEMPLATE_WELCOME = {
    'subset': 'email de boas vindas',
    'body': """
            <html>
                <body>
                    <h1> passou </h1>
                    <p> Tem anexo</p>
                    <p> tem imagem no porpo</p>
                    <img src="cid:image1">
                </body>
            </html>
    """ ,
    'image_body':{
        'id':'image1',
        'path':image_path,
        'type':'png',
        'bytes':None
    },
    'image_header':{
        'id':'image1',
        'path':image_path,
        'type':'png',
        'bytes':None
    },
    

}

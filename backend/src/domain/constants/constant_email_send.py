
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
        'path':'backend/src/domain/constants/media/estrela_pt.png',
        'type':'png',
        'bytes':None
    },
    'image_header':{
        'id':'image1',
        'path':'backend/src/domain/constants/media/estrela_pt.png',
        'type':'png',
        'bytes':None
    },
    

}

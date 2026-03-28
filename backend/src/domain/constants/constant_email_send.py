from pathlib import Path



# Mantemos as definições de diretório caso você use para outros arquivos no futuro
CURRENT_DIR = Path(__file__).parent.resolve()
MEDIA_DIR = CURRENT_DIR / "media"

# # URL Direta da Estrela (Versão PNG para maior compatibilidade com e-mail)
# URL_ESTRELA = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/PT_%28Brazil%29_logo_2021.svg/400px-PT_%28Brazil%29_logo_2021.svg.png"

# TEMPLATE_WELCOME = {
#     'subject': 'Bem-vindo ao CRM!',
#     'body': f"""
#         <html>
#             <body style="font-family: Arial, sans-serif; text-align: center;">
#                 <div style="margin: 20px auto; max-width: 600px;">
#                     <img src="{URL_ESTRELA}" alt="Logo" style="width: 150px; height: auto;">
#                     <h1 style="color: #333;">Olá, seja bem-vindo!</h1>
#                     <p style="font-size: 16px; color: #555;">Seu cadastro foi realizado com sucesso em nosso sistema.</p>
#                     <br>
#                     <img src="{URL_ESTRELA}" alt="Badge" style="width: 80px; height: auto;">
#                 </div>
#             </body>
#         </html>
#     """,
#     'images': [],  # FICAR VAZIO: Não vamos mais processar imagens locais no Adapter
#     'attachments': []
# }

# Mantemos as definições de diretório para futuras expansões
CURRENT_DIR = Path(__file__).parent.resolve()
MEDIA_DIR = CURRENT_DIR / "media"

# URL Direta da Estrela (Logo PT 2021)
URL_LOGO = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/PT_%28Brazil%29_logo_2021.svg/400px-PT_%28Brazil%29_logo_2021.svg.png"

TEMPLATE_WELCOME = {
    'subject': 'Bem-vindo(a)! Vamos juntos por São Paulo 🚩',
    'body': f"""
        <html>
            <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; background-color: #f9f9f9; margin: 0; padding: 20px;">
                <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; border: 1px solid #e0e0e0;">
                    
                    <div style="padding: 30px 20px; text-align: center; background-color: #ffffff;">
                        <img src="{URL_LOGO}" alt="Logo" style="width: 120px; height: auto;">
                    </div>

                    <div style="padding: 0 40px 30px 40px; text-align: left;">
                        <h2 style="color: #d32f2f; font-size: 24px;">Olá, ficamos felizes com seu apoio!</h2>
                        
                        <p style="font-size: 16px;">
                            Este é o canal direto para você acompanhar a caminhada do <strong>Claudinho</strong>, ex-Ouvidor de São Paulo.
                        </p>
                        
                        <p style="font-size: 16px;">
                            Sua participação é fundamental para construirmos uma cidade que sabe ouvir e agir. Por aqui, você receberá nossas propostas, agendas e convites para debates.
                        </p>

                        <div style="margin-top: 30px; padding: 20px; background-color: #fff5f5; border-radius: 5px; text-align: center;">
                            <p style="margin: 0; font-weight: bold; color: #d32f2f;">"Ouvir a cidade é o primeiro passo para mudá-la."</p>
                        </div>
                    </div>

                    <div style="padding: 20px; text-align: center; background-color: #f1f1f1; font-size: 12px; color: #777;">
                        <p style="margin: 5px 0;"><strong>Claudinho - Ex-Ouvidor de São Paulo</strong></p>
                        <p style="margin: 5px 0;">Este e-mail foi enviado porque você se cadastrou em nossa plataforma.</p>
                        <hr style="border: 0; border-top: 1px solid #ddd; margin: 15px 0;">
                        <p style="font-size: 10px;">&copy; 2026 Movimento Vamos Juntos SP</p>
                    </div>
                </div>
            </body>
        </html>
    """,
    'images': [], 
    'attachments': []
}
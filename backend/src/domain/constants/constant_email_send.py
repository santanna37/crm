from pathlib import Path

# Pega o diretório onde este arquivo está (constants/)
CURRENT_DIR = Path(__file__).parent.resolve()

# A pasta media está no mesmo nível deste arquivo
MEDIA_DIR = CURRENT_DIR / "media"

# Validação
if not MEDIA_DIR.exists():
    raise FileNotFoundError(f"Pasta media não encontrada em: {MEDIA_DIR}")

# Helper para pegar path de imagens
def get_image_path(filename: str) -> str:
    path = MEDIA_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Imagem não encontrada: {path}")
    return str(path)

TEMPLATE_WELCOME = {
    'subject': 'Bem-vindo ao CRM!',
    'body': """
        <html>
            <body style="font-family: Arial, sans-serif;">
                <img src="cid:header_logo" style="max-width: 600px;">
                <h1>Olá, seja bem-vindo!</h1>
                <p>Seu cadastro foi realizado com sucesso.</p>
                <img src="cid:body_image" style="width: 200px;">
            </body>
        </html>
    """,
    'images': [
        {'id': 'header_logo', 'path': get_image_path('estrela_pt.png'), 'type': 'png'},
        {'id': 'body_image', 'path': get_image_path('estrela_pt.png'), 'type': 'png'}
    ],
    'attachments': []  # Para arquivos não-inline
}
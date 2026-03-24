import os
import uvicorn
from src.main.server.server import app


# if __name__ == "__main__":
#   uvicorn.run(
#     "src.main.server.server:app",
#     host="0.0.0.0",
#     port=8000,
#     reload=True
#   )



if __name__ == "__main__":
    # Pega a porta do Render ou usa 8000 como fallback local
    port = int(os.environ.get("PORT", 8000))
    
    uvicorn.run(
        "src.main.server.server:app",
        host="0.0.0.0",
        port=port,  # ✅ Agora usa a porta do Render
        reload=False  # Desativa reload em produção
    )
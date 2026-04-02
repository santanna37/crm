import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pathlib import Path
from src.main.adapter.adapter_log import setup_logging
from fastapi.middleware.cors import CORSMiddleware
from src.main.routers.route_person import  router as person_router
from src.main.routers.route_log import  router as log_router


# Isso garante que as variáveis carreguem assim que o arquivo for lido
env_path = Path(__file__).parent.parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
#print(os.environ)
# -----------------------------------


app = FastAPI()

#log
setup_logging()


if os.getenv("AMBIENTE") == "LOCAL":

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(person_router)
    app.include_router(log_router)

elif os.getenv("AMBIENTE") == "ONLINE":

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["https://crm-eta-gold.vercel.app"],  
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(person_router)
    app.include_router(log_router)

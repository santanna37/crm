from fastapi import FastAPI
from sqlalchemy.orm import Session
from config.sqlalchemy.database import get_db, criar_db
from src.routers import rotascpf
# ARQUIVO PRINCIPA


#protocolos
criar_db()
app = FastAPI()


#rotas 
app.include_router(rotascpf.criar_cadastro)
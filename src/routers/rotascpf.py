# ROTAS DO CPF
#BIBLIOTECAS
from fastapi import APIRouter, Depends, status
from src.sql.schemas.cpfschema import CPFschema
from sqlalchemy.orm import Session
from src.services.sercpf import RepositorioCPF
from config.sqlalchemy.database import get_db


#ROTAS
router = APIRouter()

#criar usuario
@router.post('/cadastro')
def criar_cadastro(cpfschema: CPFschema, session: Session = Depends(get_db)):
    cpf_cadastro = RepositorioCPF(session).cadastro(cpfschema)
    return cpf_cadastro

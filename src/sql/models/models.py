# BIBLIOTECA 
from sqlalchemy import Column, String, Numeric, Boolean, Integer, Float, Date 
from config.sqlalchemy.database import Base


# BASE PRINCIPAL DE CADASTRO DE PESSOA FISICA

#modulo CPF
class CPFmodel(Base):
    __tablename__ = 'cpf'

    id = Column(Integer, autoincrement = True, primary_key = True, index = True)
    nome = Column(String)
    cpf = Column(String(14),unique = True)
    identidade = Column(String(9), unique = True)
    dataAniversario = Column(Date)
    formacao = Column(String)
    profissao = Column(String)
    endereco = Column(String)
    rua = Column(String)
    numero = Column(Integer)
    bairro = Column(String)
    cidade = Column(String)
    cep = Column(String)
    estado = Column(String) 
    telefone1 = Column(String(11))
    telefone2 = Column(String)
    email = Column(String)
    dataCriacao = Column(String)
    dataAlteracao = Column(String)


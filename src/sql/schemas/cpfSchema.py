# BIBLIOTECAS 
from pydantic import BaseModel, Field, UniqueC
from typing import Optional
from datetime import date

# SCHEMAS

class CPFschema(BaseModel):
    id: Optional[str]
    nome: str 
    cpf: str = Field(...,max_length = 14 )
    identidade: str = Field(max_length = 9)
    dataAniversario: str
    formacao = str
    profissao = str
    endereco = str 
    rua = str
    numero = str
    bairo = str
    cidade = str 
    cep = str 
    estado = str 
    telefone1 = str
    telefone2 = str
    email = str
    dataCriacao = str
    dataAlteracao = str 
        
    class config:
        orm_mode = True
# REPOSITORIO DA PESSOA FISICA
# BIBLIOTECA
from sqlalchemy.orm import Session
from src.sql.schemas.cpfschema import CPFschema
from  src.sql.models.models import CPFmodel



#criar usuario 

class RepositorioCPF():
    def __init__(self, session: Session):
        self.session = session
    
    def cadastro(self, cpf_schema: CPFschema):
        db_cpf = CPFmodel(
            id = cpf_schema.id,
            nome = cpf_schema.nome,
            cpf = cpf_schema.cpf,
            identidade = cpf_schema.identidade,
            dataAniversario = cpf_schema.dataAniversario,
            formacao = cpf_schema.formacao,
            profissao = cpf_schema.profissao,
            endereco = cpf_schema.endereco,
            rua = cpf_schema.rua,
            numero =cpf_schema.numero,
            bairo = cpf_schema.bairo,
            cidade = cpf_schema.cidade,
            cep = cpf_schema.cep,
            estado =cpf_schema.estado,
            telefone1 = cpf_schema.telefone1,
            telefone2 = cpf_schema.telefone2,
            email = cpf_schema.email,
            dataCriacao = cpf_schema.dataCriacao,
            dataAlteracao = cpf_schema.dataAlteracao
        )
        self.session.add(db_cpf)
        self.session.commit()
        self.session.refresh(db_cpf)
        return db_cpf
    
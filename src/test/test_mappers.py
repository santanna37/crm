import pytest
from datetime import date, datetime
from src.domain.models.model_person import PersonModel, AddressModel
from src.infra.db.mappers.mapper_person import PersonMapper
from src.infra.db.entities.entity_person import PersonEntity, AddressEntity


@pytest.mark.mapper
def test_domain_to_entity_conversion():
    """Deve converter um PersonModel em uma PersonEntity com sucesso"""
    
    # 1. ARRANJO (Setup do dado de entrada)
    address_mock = AddressModel(
        cep="12345-678",
        street="Rua Teste",
        number="100",
        burgh="Bairro Novo",
        city="Cidade X",
        state_uf="RJ",
        state_name="Rio de Janeiro",
        complement="Apto 1"
    )
    
    person_model = PersonModel(
        full_name="Luiz Silva",
        email="luiz@teste.com",
        birth_date=date(1995, 5, 20),
        phone="2199999999",
        created_at=datetime.now(),
        consent=True,
        activate=True,
        address=address_mock,
        themes=[] # Sua lista de descrições
    )

    # 2. AÇÃO (Executar o mapper)
    entity = PersonMapper.domain_to_entity(person_model)

    # 3. ASSERÇÃO (Verificar se os dados batem)
    assert isinstance(entity, PersonEntity)
    assert entity.full_name == person_model.full_name
    assert entity.email == person_model.email
    assert entity.consent is True
    
    # Valida se o endereço foi convertido para a Entity correta
    assert isinstance(entity.address, AddressEntity)
    assert entity.address.street == "Rua Teste"
    assert entity.address.cep == "12345-678"
    
    # Valida se a lista de temas foi repassada (como strings, conforme sua decisão)
    assert entity.themes == []
    assert isinstance(entity.themes, list)


@pytest.mark.mapper
def test_entity_to_domain_conversion():
    """Deve converter uma PersonEntity do banco de volta para o PersonModel de domínio"""
    
    # Criando uma entidade mockada (como se viesse do banco)
    address_ent = AddressEntity(id=1, street="Rua de Volta", city="Rio")
    person_ent = PersonEntity(
        id=50,
        full_name="Maria Oliveira",
        email="maria@teste.com",
        address=address_ent,
        themes=[] # Lista vazia para teste
    )
    
    # Ação
    model = PersonMapper.entity_to_domain(person_ent)
    
    # Asserção
    assert model.id == 50
    assert model.full_name == "Maria Oliveira"
    assert model.address.street == "Rua de Volta"
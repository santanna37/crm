import pytest
from datetime import date, datetime
from src.domain.models.model_person import PersonModel, AddressModel, ThemesModel
from src.infra.db.mappers.mapper_person import PersonMapper
from src.infra.db.entities.entity_person import PersonEntity, AddressEntity, Themes

@pytest.mark.mapper
def test_domain_to_entity_conversion():
    """Deve converter PersonModel (com temas) para PersonEntity"""
    
    address_mock = AddressModel(
        cep="12345-678",
        street="Rua A",
        number="10", 
        burgh="Centro",
        city="RJ",
        state_uf="RJ",
        state_name="Rio"
    )
    
    # Criamos o modelo com 2 temas
    person_model = PersonModel(
        full_name="Luiz Santanna",
        email="luiz@teste.com",
        birth_date=date(1995, 5, 20),
        phone="2199999999",
        address=address_mock,
        themes=[ThemesModel(code=1), ThemesModel(code=5)] 
    )

    entity = PersonMapper.domain_to_entity(person_model)

    # Asserções
    assert isinstance(entity, PersonEntity)
    assert entity.full_name == "Luiz Santanna"
    assert isinstance(entity.address, AddressEntity)
    
    # Validação dos Temas na Entity
    assert len(entity.themes) == 2
    assert isinstance(entity.themes[0], Themes)
    assert entity.themes[0].code == 1
    assert entity.themes[1].code == 5


@pytest.mark.mapper
def test_entity_to_domain_conversion():
    """Deve converter PersonEntity (vinda do banco) para PersonModel"""
    
    # Simulando dados do banco
    address_ent = AddressEntity(id=1, street="Rua B", city="SP", state_uf="SP")
    
    # Simulando temas vindos do banco (com ID da tabela themes)
    themes_ent = [
        Themes(id=10, code=1, id_person=50),
        Themes(id=11, code=2, id_person=50)
    ]
    
    person_ent = PersonEntity(
        id=50,
        full_name="Maria Silva",
        email="maria@teste.com",
        address=address_ent,
        themes=themes_ent,
        created_at=datetime.now()
    )
    
    model = PersonMapper.entity_to_domain(person_ent)
    
    # Asserções
    assert model.id == 50
    assert isinstance(model.address, AddressModel)
    assert model.address.street == "Rua B"
    
    # Validação dos Temas no Model
    assert len(model.themes) == 2
    assert isinstance(model.themes[0], ThemesModel)
    assert model.themes[0].code == 1
    assert model.themes[1].code == 2 # O ID da tabela themes deve voltar
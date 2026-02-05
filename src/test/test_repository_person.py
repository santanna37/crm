from src.infra.db.repositores.repository_person import PersonRepository
from src.infra.db.entities.entity_person import PersonEntity
from src.domain.models.model_person import PersonModel, AddressModel, ThemesModel
import pytest
from datetime import date


address = AddressModel(
    cep="20000-000",
    street="Rua Teste",
    number="123",
    city="Rio de Janeiro",
    burgh="ribeira",
    state_uf="RJ",
    state_name="Rio de Janeiro",
)

person_test = PersonModel(
    full_name="Luiz Santanna",
    email="luiz@email.com",
    birth_date=date(1995, 5, 20),
    phone="21999999999",
    consent=True,
    address=address,
    themes= [ThemesModel(code=1), ThemesModel(code=2)]
)

@pytest.mark.repo
def test_repo_create_person():
    repo = PersonRepository()
    repo.create_person(person= person_test)
    print('passou_create_test')


# # def test_repo_list_person():
# #     repo = PersonRepository()
# #     lista = repo.read_person(name = user_test.name)
# #     print(f'read_passou_test = {lista}')


# # def test_repo_update_person():
# #     repo = PersonRepository()
# #     lista = repo.update_person(name= user_test.name, new_data= user_test2)
# #     print(lista)
# #     print('passou_update_test')
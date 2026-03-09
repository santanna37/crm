from dataclasses import dataclass, field, asdict
from typing import Optional, List
from datetime import date, datetime




@dataclass
class AddressModel:
    cep: str
    street: str
    number: str
    burgh: str
    city: str
    state_uf: str
    state_name: str
    complement: str = ''
    id: int |None = None


@dataclass
class ThemesModel:
    code: int 
    id: int | None = None

@dataclass
class PersonModel:
    full_name: str
    email: str
    birth_date: date
    phone: str
    address: AddressModel
    themes: List[ThemesModel] = field(default_factory=list)
    created_at:Optional[datetime] = None
    consent: bool = False
    activate: bool = True
    id: int |None = None


filter = PersonModel(
    full_name="Luizinho",
    email="teste@teste.com",
    birth_date="21/21/2222",
    phone=None,
    address=AddressModel(cep="21930007",
                        street=None, 
                        number=None,
                        burgh=None,
                        city=None,
                        state_uf=None,
                        state_name=None),
    themes=[ThemesModel(code=1)]
)

filter_http = { 
    'full_name':"Luizinho",
    'email':"teste@teste.com",
    'birth_date':"21/21/2222",
    'phone':None,
    #'cep':"21930007",
    'street':None, 
    'number':None,
    'burgh':None,
    #'city':None,
    'state_uf':None,
    'state_name':None,
    'themes':[1,2]
}


address = AddressModel(
    cep="20000-000",
    street="Rua Teste",
    number="999",
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
    themes= [ThemesModel(code=0), ThemesModel(code=2)],
    created_at=datetime(2026, 1, 20, 21, 44, 58)
)
lista = [person_test]

def dto_response(person_list:List) -> dict:

    response_data = []
    for person in person_list:
        # Transforma em dicionário
        person_dict = asdict(person)
        
        # Limpa as datas para String (ISO)
        if isinstance(person_dict.get("birth_date"), (date, datetime)):
            person_dict["created_at"] = person_dict["created_at"].isoformat()
            person_dict["birth_date"] = person_dict["birth_date"].isoformat()
        
        response_data.append(person_dict)
        
    return print(response_data)

dto_response(lista)


# def dto_person_read(filters:dict):
#     filter_person = PersonModel.__annotations__.keys()
#     filter_address = AddressModel.__annotations__.keys()
#     filter_themes = ThemesModel.__annotations__.keys()
#     dto_filter_address = {}
#     dto_filter_person = {}
#     dto_filter_themes = []
#     themes_dict = {}
    
#     for key in filter_address:
#         dto_filter_address[f"{key}"] = filters.get(f"{key}",None)

#     for key in filter_person:
#         dto_filter_person[f"{key}"] = filters.get(f"{key}",None)
        
#     print("teste_adress",dto_filter_address)
#     print("teste_person", dto_filter_person)

# dto_person(filters=filter_http) 

    
    

# def read_person(self, filters:PersonModel)->List:
#     filters = asdict(filters)
#     filters_themes = filters["themes"]
#     filters_address = filters["address"]
#     filters.pop("address")
#     filters.pop("themes")
#     print("themes", filters_themes)
#     print("endereço",filters_address)
#     print("dados",  filters)
#     list_filter = []
#     theme_conditions = []
#     with DBConnectionHandler() as session:
#         try:
#             query = session.query(PersonEntity).outerjoin(AddressEntity).outerjoin(Themes)
            
#             for key, value in filters.items():
#                 if value:
#                     columm = getattr(PersonEntity, key)
#                     query = query.filter(columm.like(f"%{value}%"))
            
#             for key, value in filters_address.items():
#                 if value:
#                     columm = getattr(AddressEntity, key)
#                     query = query.filter(columm.like(f"%{value}%"))
            
#             for theme in filters_themes: 
#                 for key, value in theme.items():
#                     if value:
#                         columm = getattr(Themes, key)
#                         theme_conditions.append(columm == value)
#             if theme_conditions:
#                 query = query.filter(or_(*theme_conditions))
                
#             response = query.distinct().all()

#             for item in response:
#                 list_filter.append(item)
            
#             return list_filter

#         except Exception as exception:
#             print(f"Erro na query: {exception}")
#             raise exception
#       #      query = query.filter(key.like(f"%{value}%"))
            

# read_person(filter=filter)
# read(filter)


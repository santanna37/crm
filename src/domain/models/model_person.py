from dataclasses import dataclass
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
    code: str = 'outros'
    description: str = 'Outros'
    id: int = 15

@dataclass
class PersonModel:
    full_name: str
    email: str
    birth_date: date
    created_at: datetime
    phone: str
    address: AddressModel
    themes: List[ThemesModel]
    consent: bool = False
    activate: bool = True
    id: int |None = None

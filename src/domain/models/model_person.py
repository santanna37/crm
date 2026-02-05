from dataclasses import dataclass, field
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

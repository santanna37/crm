from src.presentation.validator.validator_person import PersonValidator
from src.domain.models.model_person import PersonModel, AddressModel, ThemesModel

from dataclasses import asdict
from datetime import date, datetime
from typing import List, Dict


class DTOPerson:

    def __init__(self, validator: PersonValidator) -> None:

        self._validator = validator
    
    
    def dto_person_create(self, person_dict: Dict) -> PersonModel:
        """ 
        Recebe dados do html.body
        """

        full_name = self._validator.name_validator(name = person_dict.get("full_name"))
        email = self._validator.email_validador(email_person = person_dict.get("email"))
        birth_date = self._validator.birth_date_validator(birth_date_person = person_dict.get("birth_date"))
        phone = self._validator.phone_validator(phone_person = person_dict.get("phone"))
        consent = person_dict.get("consent")
        
        # lista temas
        themes_list = []
        themes = self._validator.themes_validator(themes_names = person_dict.get("themes"))
        for theme in themes:
            themes_list.append(ThemesModel(code= theme))

        # address vem do request -> sem validação 
        address = person_dict.get("address", {})

        address_data = AddressModel(
                                    cep = address.get("cep"),
                                    street = address.get("street"),
                                    number = address.get("number"),
                                    burgh = address.get("burgh"),
                                    city = address.get("city"),
                                    state_name = address.get("state_name"),
                                    state_uf = address.get("state_uf"),
                                    complement = address.get("complement")
        )

        body_person = PersonModel(
                                full_name = full_name,
                                email = email,
                                birth_date = birth_date,
                                phone = phone,
                                address = address_data,
                                themes = themes_list,
                                consent = consent
        )

        return body_person


    
    def dto_person_read(self, filters: Dict) -> PersonModel:

        #contrução do PersonMModels
        # themes
        themes_list = []
        themes = self._validator.themes_validator(themes_names=filters.get("themes"))
        for theme in themes:
            themes_list.append(ThemesModel(code=theme))
                    
        filter_person = PersonModel.__annotations__.keys()
        filter_address = AddressModel.__annotations__.keys()
        
        dto_filter_address = {}
        dto_filter_person = {}
        
        for key in filter_address:
            dto_filter_address[f"{key}"] = filters.get(f"{key}",None)

        for key in filter_person:
            dto_filter_person[f"{key}"] = filters.get(f"{key}",None)

        filters_address = AddressModel(
                                        cep = dto_filter_address.get("cep"),
                                        street = dto_filter_address.get("street"),
                                        number = dto_filter_address.get("number"),
                                        burgh = dto_filter_address.get("burgh"),
                                        city = dto_filter_address.get("city"),
                                        state_uf = dto_filter_address.get("state_uf"),
                                        state_name = dto_filter_address.get("state_name"),
                                        complement = dto_filter_address.get("complent")
        )

        dto_filters_person = PersonModel(
                                        full_name = dto_filter_person.get("full_name"),
                                        email = dto_filter_person.get("email"),
                                        birth_date = dto_filter_person.get("birth_date"),
                                        phone = dto_filter_person.get("phone"),
                                        address = filters_address,
                                        themes = themes_list,
                                        consent = dto_filter_person.get("consent"),
                                        activate = dto_filter_person.get("activate")
        )

        return dto_filters_person


    def dto_person_read_response(self, person_list: List) -> List[Dict]:
        """
        Trata os dados de domínio para o formato que a Web (JSON) entende.
        """
        response_data = []
        for person in person_list:
            # Transforma em dicionário
            person_dict = asdict(person)
            
            # Limpa as datas para String (ISO)
            if isinstance(person_dict.get("birth_date"), (date, datetime)):
                person_dict["created_at"] = person_dict["created_at"].isoformat()
                person_dict["birth_date"] = person_dict["birth_date"].isoformat()
            
            response_data.append(person_dict)
            
        return response_data
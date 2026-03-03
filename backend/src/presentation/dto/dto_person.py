from src.presentation.validator.validator_person import PersonValidator
from src.domain.models.model_person import PersonModel, AddressModel, ThemesModel
from typing import Dict


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

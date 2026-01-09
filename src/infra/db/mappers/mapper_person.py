from typing import Dict
from src.domain.models.model_person import PersonModel, AddressModel, ThemesModel
from src.infra.db.entities.entity_person import PersonEntity, AddressEntity, Themes


class PersonMapper:

    @staticmethod
    def domain_to_entity(model: PersonModel) -> PersonEntity:
        
        address_person = AddressEntity(
            cep = model.address.cep,
            street = model.address.street,
            number = model.address.number,
            complement = model.address.complement,
            burgh = model.address.burgh,
            city = model.address.city,
            state_uf = model.address.state_uf,
            state_name = model.address.state_name
        )
        
        return PersonEntity(
            full_name = model.full_name,
            email=model.email,
            birth_date = model.birth_date,
            phone = model.phone,
            consent = model.consent,
            created_at = model.created_at,
            activate = model.activate,
            address = address_person,
            themes = model.themes
        )

    @staticmethod
    def entity_to_domain(entity: PersonEntity) -> PersonModel:



        return PersonModel(
            id = entity.id,
            full_name = entity.full_name,
            email=entity.email,
            birth_date = entity.birth_date,
            phone = entity.phone,
            consent = entity.consent,
            created_at = entity.created_at,
            activate = entity.activate,
            address = entity.address,
            themes = entity.themes
        )

    # @staticmethod
    # def dict_to_domain(data: Dict) -> PersonModel:
    #     return PersonModel(
    #         id=data.get("id"),
    #         name=data.get("name"),
    #         email=data.get("email")
    #     )

    # @staticmethod
    # def domain_to_dict(model: PersonModel) -> Dict:
    #     return {
    #         "id": model.id,
    #         "name": model.name,
    #         "email": model.email
    #     }

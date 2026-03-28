from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.mappers.mapper_person import PersonMapper
from src.infra.db.entities.entity_person import PersonEntity, AddressEntity, Themes
from src.domain.models.model_person import PersonModel, AddressModel, ThemesModel
from src.data.interface.repository_person_interface import PersonRepositoryInterface

from dataclasses import asdict
from typing import List
from sqlalchemy import or_


class PersonRepository(PersonRepositoryInterface):

    def create_person(self,person: PersonModel) -> PersonModel:

        new_user = PersonMapper.domain_to_entity(model = person)

        with DBConnectionHandler() as session:
            try:
                print(f"🔍 [DEBUG] Tentando salvar: {new_user}")
                session.add(new_user)
                session.commit()
                print(f"✅ [DEBUG] Commit realizado com sucesso!")
                session.refresh(new_user)
                
                return PersonMapper.entity_to_domain(new_user)

            except Exception as exception:
                print(f"❌ [DEBUG] Erro ao salvar: {exception}")
                session.rollback()

                raise exception


    def read_person(self, filters:PersonModel)->List:

        filters = asdict(filters)
        filters_themes = filters["themes"]
        filters_address = filters["address"]
        filters.pop("address")
        filters.pop("themes")
        
        list_filter = []
        theme_conditions = []
        with DBConnectionHandler() as session:
            try:
                query = session.query(PersonEntity).outerjoin(AddressEntity).outerjoin(Themes)
                
                for key, value in filters.items():
                    if value:
                        column = getattr(PersonEntity, key)
                        if isinstance(value, str):
                            query = query.filter(column.like(f"%{value}%"))
                        else:
                            query = query.filter(column == value)
                
                for key, value in filters_address.items():
                    if value:
                        column = getattr(AddressEntity, key)
                        if isinstance(value, str):
                            query = query.filter(column.like(f"%{value}%"))
                        else:
                            query = query.filter(column == value)
                
                for theme in filters_themes: 
                    for key, value in theme.items():
                        if value is not None:
                            column = getattr(Themes, key)
                            theme_conditions.append(column == value)
                if theme_conditions:
                    query = query.filter(or_(*theme_conditions))
                
                print(str(query.statement))
                print(query)
                response = query.distinct().all()

                for item in response:
                    list_filter.append(PersonMapper.entity_to_domain(item))
                print(f"[DEBUG_QUERY] - {list_filter}")
                print(len(list_filter))
                
                return list_filter

            except Exception as exception:
                print(f"Erro na query: {exception}")
                raise exception


    # def update_person(self, name: str, new_data:PersonModel) -> PersonModel:
    #     with DBConnectionHandler() as database:
    #         try:
    #             quest =(
    #                 database
    #             .query(PersonEntity)
    #             .filter(PersonEntity.name == name)
    #             .first()
    #             )

    #             if not quest:
    #                 return None
                
    #             new_data = new_data.__dict__
                
    #             for key, value in new_data.items():
    #                 if value is not None:
    #                     setattr(quest,key,value)
                
    #             database.commit()
    #             database.refresh(quest)

    #             update_person = PersonMapper.entity_to_domain(quest)
    #             return update_person

    #         except Exception as exception:
    #             database.rollback()
    #             return exception

    #         finally:
    #             print('update_acabou')
    #             database.close()





    #def delete_person(name: str) -> PersonModel:pass 

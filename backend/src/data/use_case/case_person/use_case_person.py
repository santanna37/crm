from src.data.interface.repository_person_interface import PersonRepositoryInterface
from src.domain.models.model_person import PersonModel
from src.domain.use_case.case_person.use_case_person_interface import UseCasePersonInterface
from typing import List, Dict
from src.infra.db.mappers.mapper_person import PersonMapper
from src.domain.use_case.case_email.use_case_email_interface import UseCaseEmailInterface
from src.domain.constants.constant_email_send import TEMPLATE_WELCOME, get_welcome_template
from fastapi import BackgroundTasks


class UseCasePerson(UseCasePersonInterface):

    def __init__(self, repository: PersonRepositoryInterface,
                        email_service: UseCaseEmailInterface = None):
        self.__email_service = email_service
        self.__repository = repository

    def health(self) -> str:
        cash_email = get_welcome_template()
        print(f"[CHECK_CASH] Email carregado - {len(cash_email)}")
        self.__repository.health_check()


    def create(self, person: PersonModel, background_tasks:BackgroundTasks = None) -> Dict:
        new_person = self.__repository.create_person(person= person)

        if self.__email_service and background_tasks:
            try:
                background_tasks.add_task(
                    self.__email_service.welcome_email,
                            email= person.email,
                            email_class=TEMPLATE_WELCOME,
                )
            except Exception as error:
                print(f"[DEBUG] Falha no envio do email {error}")

        return new_person

    def read(self, filters:PersonModel) -> List:
        list_person = self.__repository.read_person(filters= filters)

        return list_person

    # def update(self, name:str, new_data:PersonModel) -> str:
    #     up_person = self.__repository.update_person(name= name, new_data= new_data)

    #     return up_person  
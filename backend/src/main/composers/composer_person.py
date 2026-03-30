from src.infra.db.repositores.repository_person import PersonRepository
from src.data.use_case.case_person.use_case_person import UseCasePerson
from src.presentation.controllers.controller_person import CreatePersonController, ReadPersonController, HealthCheckController
from src.presentation.dto.dto_person import DTOPerson
from src.presentation.validator.validator_person import PersonValidator
from src.data.use_case.case_email.use_case_email import UseCaseEmail
from src.main.adapter.adapter_email import AdapterEmail


class PersonCompose:

    @staticmethod
    def check_health():
        repository = PersonRepository()
        use_case = UseCasePerson(repository= repository, email_service= None)
        controller = HealthCheckController(use_case= use_case)
        return controller

    @staticmethod
    def person_register():
        email_adapter = AdapterEmail()
        email_welcome = UseCaseEmail(adapter= email_adapter)
        

        validator = PersonValidator()
        dto = DTOPerson(validator= validator)

        repository = PersonRepository()
        use_case = UseCasePerson(repository= repository, email_service= email_welcome)
        controller = CreatePersonController(use_case= use_case,dto= dto)

        return controller

    @staticmethod
    def person_read():
        validator = PersonValidator()
        dto = DTOPerson(validator=validator)
        
        repository = PersonRepository()
        use_case = UseCasePerson(repository= repository, email_service= None)
        controller = ReadPersonController(use_case=use_case, dto= dto)

        return controller


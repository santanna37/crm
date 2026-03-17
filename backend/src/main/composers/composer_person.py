from src.infra.db.repositores.repository_person import PersonRepository
from src.data.use_case.case_person.use_case_person import UseCasePerson
from src.presentation.controllers.controller_person import CreatePersonController, ReadPersonController
from src.presentation.dto.dto_person import DTOPerson
from src.presentation.validator.validator_person import PersonValidator
from src.data.use_case.case_email.use_case_email import UseCaseEmail


class PersonCompose:

    @staticmethod
    def person_register():

        validator = PersonValidator()
        dto = DTOPerson(validator= validator)

        repository = PersonRepository()
        email_welcome = UseCaseEmail()
        use_case = UseCasePerson(repository= repository, email_service= email_welcome)
        controller = CreatePersonController(use_case= use_case,dto= dto)

        return controller

    @staticmethod
    def person_read():
        validator = PersonValidator()
        dto = DTOPerson(validator=validator)
        
        repository = PersonRepository()
        use_case = UseCasePerson(repository= repository)
        controller = ReadPersonController(use_case=use_case, dto= dto)

        return controller


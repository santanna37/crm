from src.presentation.validator.validator_person import PersonValidator
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.use_case.case_person.use_case_person_interface import UseCasePersonInterface
from src.presentation.interfaces.controller_person_interface import CreatePersonControllerInterface, ReadPersonControllerInterface
from src.presentation.dto.dto_person import DTOPerson
from src.infra.db.mappers.mapper_person import PersonMapper
from src.presentation.http_types.status_code import HTTPStatus

from dataclasses import asdict


class  CreatePersonController(CreatePersonControllerInterface):


    def __init__(self, use_case: UseCasePersonInterface, dto: DTOPerson):
        self._use_case = use_case
        self._dto = dto

    def handler(self, http_request: HttpRequest) -> HttpResponse:

        try:
            person_model = self._dto.dto_person_create(person_dict= http_request.body)
            result = self._use_case.create(person= person_model)
            # envio do email
            return HttpResponse(status_code = HTTPStatus.CREATED, body = 'created')

        except Exception as error:
            return HttpResponse(status_code = HTTPStatus.BAD_REQUEST,
                                body= { 'error': str(error)})


class ReadPersonController:

    def __init__(self, use_case: UseCasePersonInterface, dto: DTOPerson):
        self.__use_case = use_case
        self.__dto = dto
    
    def handler(self, http_request: HttpRequest) -> HttpResponse:

        try:
            person_model = self.__dto.dto_person_read(filters= http_request.query_params)
            result = self.__use_case.read(filters=person_model)

            response = self.__dto.dto_person_read_response(person_list= result)
            

            return HttpResponse(status_code=HTTPStatus.ACCEPTED, body = response)
        
        except Exception as error:
            return HttpResponse(status_code = HTTPStatus.BAD_REQUEST, body={'error': str(error)})




# from src.main.composers.composer_person import PersonCompose
# from src.presentation.http_types.http_request import HttpRequest
# from src.presentation.http_types.status_code import HTTPStatus
# import pytest



# @pytest.mark.integration
# class TestCreatePersonController:
    
#     def test_handler_create_person_success(self):
#         """Deve criar uma pessoa com sucesso e retornar 201"""
        
#         # Arranjo
#         controller = PersonCompose.person_register()
        
        # mock_body = {
        #     "full_name": "Luiz Santanna Integration",
        #     "email": f"integration_{pytest.importorskip('time').time()}@test.com", # Email dinâmico para evitar erro de Unique
        #     "birth_date": "1995-10-10",
        #     "phone": "21999998888",
        #     "consent": True,
        #     "themes": ["Saúde", "Educação"],
        #     "address": {
        #         "cep": "20000-000",
        #         "street": "Rua de Integração",
        #         "number": "500",
        #         "burgh": "Centro",
        #         "city": "Rio de Janeiro",
        #         "state_name": "Rio de Janeiro",
        #         "state_uf": "RJ",
        #         "complement": "Apto 101"
        #     }
        # }
        
#         request = HttpRequest(body=mock_body)

#         # Ação
#         response = controller.handler(request)
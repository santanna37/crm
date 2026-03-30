from fastapi import Request, BackgroundTasks
from fastapi.responses import JSONResponse
from src.presentation.http_types.http_request import HttpRequest
from src.main.composers.composer_person import PersonCompose




async def system_check_health():

    controller = PersonCompose.check_health()

    http_request = HttpRequest()

    http_response = controller.handler(http_request=http_request)

    return JSONResponse(status_code= http_response.status_code,content=http_response.body)


async def person_adapter_create(request: Request, background_tasks: BackgroundTasks=None):
    
    body = await request.json()

    http_request = HttpRequest(body= body)

    handler = PersonCompose.person_register()

    http_response = handler.handler(http_request= http_request, background_tasks=background_tasks)

    return JSONResponse(status_code= http_response.status_code,
                        content= http_response.body)


async def person_adapter_read(request: Request):

    filters = dict(request.query_params)

    http_request = HttpRequest(query_params= filters)

    handler = PersonCompose.person_read()

    http_response = handler.handler(http_request= http_request)

    return JSONResponse(status_code= http_response.status_code,
                        content= http_response.body)
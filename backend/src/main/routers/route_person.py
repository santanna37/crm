from fastapi import APIRouter, Request, BackgroundTasks
from  src.main.adapter.adapter_person import person_adapter_create, person_adapter_read


router = APIRouter(prefix="/person", tags=["Person"])



@router.post("/")
async def create_person_router(request: Request, background_tasks: BackgroundTasks=None):
    return await person_adapter_create(request=request)
    

@router.get("/list")
async def read_person_router(request: Request):
    return await person_adapter_read(request=request)   
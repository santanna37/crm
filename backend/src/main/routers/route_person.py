from fastapi import APIRouter, Request, BackgroundTasks, Depends
from  src.main.adapter.adapter_person import person_adapter_create, person_adapter_read, system_check_health
from src.main.middleware.auth_middleware import verify_admin


router = APIRouter(prefix="/person", tags=["Person"])



# ROTA PUBLICA
@router.post("/")
async def create_person_router(request: Request, background_tasks: BackgroundTasks=None):
    return await person_adapter_create(request=request)
    

# ROTA PRIVADA
@router.get("/list")
async def read_person_router(request: Request, current_user: dict = Depends(verify_admin)):
    return await person_adapter_read(request=request)   
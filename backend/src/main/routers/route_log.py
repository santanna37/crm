from fastapi import APIRouter
from src.main.adapter.adapter_log import log_buffer
from  src.main.adapter.adapter_person import system_check_health


router = APIRouter(prefix="/system", tags=["System"])


@router.get("/health")
async def health_check_router(): 
    return await system_check_health()

@router.get("/logs")
async def get_log_router():
    return list(log_buffer)
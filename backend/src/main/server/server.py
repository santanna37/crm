from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.main.routers.route_person import  router as person_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois restringimos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(person_router)




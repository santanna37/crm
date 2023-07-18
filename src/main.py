from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from config.sqlalchemy.database import get_db, criar_db

# ARQUIVO PRINCIPA
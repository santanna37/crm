from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pathlib import Path
import os


# Isso garante que as variáveis carreguem assim que o arquivo for lido
env_path = Path(__file__).parent.parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
# -----------------------------------


class DBConnectionHandler:
    def __init__(self) -> None:
        # URL sem nenhum parâmetro extra
        self.__conection_string = os.getenv("DATABASE_URL") or os.getenv("DATABASE_URL_LOCAL") 
        # --- INCLUIR ESTE DEBUG AQUI ---
        if self.__conection_string:
            # Isso vai mascarar sua senha para não vazar no log, mas mostrar o host
            host = self.__conection_string.split("@")[-1]
            print(f"🚀 [DEBUG] Conectando ao Banco em: {host}")
        else:
            print("⚠️ [DEBUG] Nenhuma URL de banco encontrada no .env!")
        # -------------------------------
        
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(
            self.__conection_string,
            connect_args={
                "connect_timeout": 10
            }
        )
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind = self.__engine)
        self.session = session_make()
        return self.session

    def __exit__(self, exc_type, exc_val,  exc_tb):
        if self.session:
            self.session.close()


#mysql+pymysql://root:senha@127.0.0.1:3301/public?charset=utf8mb4&allowPublicKeyRetrieval=true

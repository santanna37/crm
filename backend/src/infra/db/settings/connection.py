from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pathlib import Path
import os


# Isso garante que as variáveis carreguem assim que o arquivo for lido
env_path = Path(__file__).parent.parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
#print(os.environ)
# -----------------------------------




class DBConnectionHandler:
    def __init__(self) -> None:
        if os.getenv("AMBIENTE") == "LOCAL":
            self.__conection_string = os.getenv("DATABASE_URL_LOCAL")         

            if self.__conection_string:
                host = os.getenv("AMBIENTE")
                print(f"🚀 [DEBUG_CONNECTION] Conectando ao Banco em: {host}")
            else:
                print("⚠️ [DEBUG_CONNECTION] Nenhuma URL de banco encontrada no .env!")

        elif os.getenv("AMBIENTE") == "ONLINE":
            self.__conection_string = os.getenv("DATABASE_URL")

            if self.__conection_string:
                host = os.getenv("AMBIENTE")
                print(f"🚀 [DEBUG_CONNECTION] Conectando ao Banco em: {host}")
            else:
                print("⚠️ [DEBUG_CONNECTION] Nenhuma URL de banco encontrada no .env!")
        
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

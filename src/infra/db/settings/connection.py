from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__conection_string =("mysql+pymysql://root:senha@127.0.0.1:3301/public"
    "?charset=utf8mb4"
        )

        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(
            self.__conection_string,
            pool_pre_ping=True,
            pool_recycle=3000,
            pool_size=5,
            max_overflow=10,
            connect_args={
                "connect_timeout":10
            },
            echo=False
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

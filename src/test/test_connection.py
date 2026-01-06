from src.infra.db.settings.connection import DBConnectionHandler
from sqlalchemy import text 
import pytest



@pytest.mark.integration
def test_create_engine_database():
    db_connection = DBConnectionHandler()
    engine = db_connection.get_engine()


@pytest.mark.integration
def test_work_engine_database():
    db_connection = DBConnectionHandler()
    engine = db_connection.get_engine()

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1



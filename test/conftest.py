import pytest
from src.init_db import apply_schema

@pytest.fixture(scope="session", autouse=True)
def preparar_esquema():
    apply_schema()
    yield

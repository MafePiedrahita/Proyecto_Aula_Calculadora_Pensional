import pytest
from src.model.conexion_db import db_cursor

@pytest.fixture(autouse=True)
def limpiar_tablas():
    """
    Limpia las tablas antes de cada prueba para evitar conflictos de datos previos.
    Se ejecuta automáticamente antes de cada test.
    """
    with db_cursor() as (conn, cur):
        # El orden importa si hay claves foráneas
        cur.execute("DELETE FROM simulacion;")
        cur.execute("DELETE FROM cotizacion;")
        cur.execute("DELETE FROM aportante;")

# test/conftest.py
import pytest
from datetime import date
from src.model.conexion_db import db_cursor
from src.model.entities.aportante import Aportante
from src.controller import aportante_controller as ac

@pytest.fixture(autouse=True)
def limpiar_tablas():
    """
    Se ejecuta antes de cada test. Deja las tablas limpias.
    El orden importa por claves foráneas.
    """
    with db_cursor() as (conn, cur):
        cur.execute("DELETE FROM simulacion;")
        cur.execute("DELETE FROM cotizacion;")
        cur.execute("DELETE FROM aportante;")

@pytest.fixture
def aportante_base():
    """
    Crea un aportante válido y retorna su ID para usar en tests
    que requieren un aportante existente.
    """
    ap = Aportante(
        None, 'CC', 'DOC-TST-BASE', 'Test', 'User',
        date(1990, 1, 1), 2_000_000, 1400, 35   # semanas>=1300 para sim. pública
    )
    return ac.crear(ap)


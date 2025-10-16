from datetime import date
import pytest
from src.model.entities.aportante import Aportante
from src.model.entities.cotizacion import Cotizacion
from src.controller import aportante_controller as ac
from src.controller import cotizacion_controller as cc

@pytest.fixture
def aportante_id():
    return ac.crear(Aportante(None,'CC','DOC-COTZ','Cot','Apo',date(1990,1,1),2_000_000,800,34))

def test_crear_listar_actualizar(aportante_id):
    cid = cc.crear(Cotizacion(None, aportante_id, None, 0.0, 200, date(2020,1,1), date(2021,1,1)))
    assert cid > 0
    assert len(cc.listar_por_aportante(aportante_id)) >= 1
    assert cc.actualizar(Cotizacion(cid, aportante_id, None, 5_000_000, 300, date(2020,1,1), date(2022,1,1))) == 1

def test_error_rango(aportante_id):
    with pytest.raises(Exception):
        cc.crear(Cotizacion(None, aportante_id, None, 0.0, 100, date(2021,1,1), date(2020,1,1)))

from datetime import date
import pytest
from src.model.entities.cotizacion import Cotizacion
from src.controller import cotizacion_controller as cc

def test_crear_listar_actualizar(aportante_base):
    ap_id = aportante_base

    cid = cc.crear(Cotizacion(
        None, ap_id, None, 0.0, 200, date(2020, 1, 1), date(2021, 1, 1)
    ))
    assert cid > 0

    listado = cc.listar_por_aportante(ap_id)
    assert isinstance(listado, list)
    assert len(listado) >= 1

    afectadas = cc.actualizar(Cotizacion(
        cid, ap_id, None, 5_000_000, 300, date(2020, 1, 1), date(2022, 1, 1)
    ))
    assert afectadas == 1

def test_error_rango(aportante_base):
    ap_id = aportante_base
    with pytest.raises(Exception):
        cc.crear(Cotizacion(
            None, ap_id, None, 0.0, 100, date(2021, 1, 1), date(2020, 1, 1)
        ))

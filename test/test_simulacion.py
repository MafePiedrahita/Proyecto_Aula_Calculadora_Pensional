from datetime import date
import pytest
from src.model.entities.aportante import Aportante
from src.controller import aportante_controller as ac
from src.service.simulacion_service import estimar_publico, estimar_privado

def test_sim_publico_ok():
    ap_id = ac.crear(Aportante(None,'CC','DOC-PUB','Pub','Ok',date(1985,1,1),2_000_000,1400,40))
    assert estimar_publico(ap_id, 0.65) > 0

def test_sim_publico_error():
    ap_id = ac.crear(Aportante(None,'CC','DOC-PUB-ERR','Pub','Err',date(1985,1,1),2_000_000,200,40))
    with pytest.raises(ValueError):
        estimar_publico(ap_id)

def test_sim_privado_ok():
    ap_id = ac.crear(Aportante(None,'CC','DOC-PRIV','Priv','Ok',date(1985,1,1),2_000_000,800,40))
    assert estimar_privado(ap_id, 120_000_000, 240) > 0

def test_sim_privado_error():
    ap_id = ac.crear(Aportante(None,'CC','DOC-PRIV-ERR','Priv','Err',date(1985,1,1),2_000_000,800,40))
    with pytest.raises(ValueError):
        estimar_privado(ap_id, -1)

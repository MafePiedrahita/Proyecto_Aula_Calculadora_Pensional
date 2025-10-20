import pytest
from src.service.simulacion_service import estimar_publico, estimar_privado

def test_sim_publico_ok(aportante_base):
    ap_id = aportante_base
    sim_id = estimar_publico(ap_id, 0.65)
    assert sim_id > 0

def test_sim_publico_error(aportante_base, monkeypatch):
    """
    Fuerza semanas < 1300 para provocar el error de RPM.
    Si no quieres monkeypatch, crea otra fixture de aportante con pocas semanas.
    """
    from src.controller import aportante_controller as ac
    ap = ac.buscar_por_id(aportante_base)
    ap.semanas_cot = 1200
    # Simulamos que buscar_por_id devuelva este objeto modificado
    monkeypatch.setattr("src.service.simulacion_service.buscar_por_id", lambda _id: ap)
    with pytest.raises(ValueError):
        estimar_publico(aportante_base, 0.65)

def test_sim_privado_ok(aportante_base):
    ap_id = aportante_base
    sim_id = estimar_privado(ap_id, 50_000_000, 240)
    assert sim_id > 0

def test_sim_privado_error(aportante_base):
    ap_id = aportante_base
    with pytest.raises(Exception):
        estimar_privado(ap_id, -1, 240)   # saldo inválido

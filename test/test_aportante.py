from datetime import date
import pytest
from src.model.entities.aportante import Aportante
from src.controller import aportante_controller as ac

def test_insert_ok():
    ap = Aportante(None,'CC','DOC-100','Ana','Lopez',date(1990,5,1),2_500_000,1500,35)
    assert ac.crear(ap) > 0

def test_insert_error_salario():
    ap = Aportante(None,'CC','DOC-ERR','Err','Neg',date(1995,1,1),-1,500,28)
    with pytest.raises(Exception):
        ac.crear(ap)

def test_select_ok_y_no_existe():
    ap = Aportante(None,'CC','DOC-200','Clau','Ram',date(1992,2,2),1_800_000,1200,31)
    ap_id = ac.crear(ap)
    assert ac.buscar_por_id(ap_id).nro_doc == 'DOC-200'
    assert ac.buscar_por_id(999999) is None

def test_update_y_delete():
    ap = Aportante(None,'CC','DOC-300','Del','Me',date(1990,1,1),1_000_000,1000,34)
    ap_id = ac.crear(ap)
    assert ac.actualizar_salario(ap_id, 2_000_000) == 1
    assert ac.eliminar(ap_id) == 1

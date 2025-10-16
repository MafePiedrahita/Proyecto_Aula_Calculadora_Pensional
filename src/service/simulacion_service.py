from src.model.entities.simulacion import Simulacion
from src.controller.aportante_controller import buscar_por_id
from src.controller.simulacion_controller import insertar as insertar_sim

def estimar_publico(aportante_id: int, tasa_reemplazo: float = 0.65) -> int:
    ap = buscar_por_id(aportante_id)
    if not ap:
        raise ValueError("Aportante no existe")
    if ap.semanas_cot < 1300:
        raise ValueError("Semanas insuficientes para RPM (>= 1300 en esta demo)")
    pension = round(ap.salario_prom * tasa_reemplazo, 2)
    sim = Simulacion(None, aportante_id, 'PUBLICO',
                     pension, {"tasa_reemplazo": tasa_reemplazo})
    return insertar_sim(sim)

def estimar_privado(aportante_id: int, saldo: float, factor_renta: float = 240) -> int:
    if saldo < 0:
        raise ValueError("Saldo no puede ser negativo")
    pension = round(saldo / factor_renta, 2)
    sim = Simulacion(None, aportante_id, 'PRIVADO',
                     pension, {"factor_renta": factor_renta})
    return insertar_sim(sim)

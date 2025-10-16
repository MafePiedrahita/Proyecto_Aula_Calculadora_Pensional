from decimal import Decimal, ROUND_HALF_UP
from src.model.entities.simulacion import Simulacion
from src.controller.aportante_controller import buscar_por_id
from src.controller.simulacion_controller import insertar as insertar_sim

def _to_decimal(n) -> Decimal:
    """
    Convierte enteros/floats/strings/Decimal a Decimal de forma segura.
    - Para floats, usa str(n) para evitar problemas binarios.
    """
    if isinstance(n, Decimal):
        return n
    if isinstance(n, (int,)):
        return Decimal(n)
    if isinstance(n, float):
        return Decimal(str(n))
    return Decimal(n)  # para strings

def estimar_publico(aportante_id: int, tasa_reemplazo: float = 0.65) -> int:
    ap = buscar_por_id(aportante_id)
    if not ap:
        raise ValueError("Aportante no existe")
    if ap.semanas_cot < 1300:
        raise ValueError("Semanas insuficientes para RPM (>= 1300 en esta demo)")

    salario = _to_decimal(ap.salario_prom)
    tasa = _to_decimal(tasa_reemplazo)

    # Redondeo a 2 decimales (mitad hacia arriba)
    pension = (salario * tasa).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    sim = Simulacion(
        None,
        aportante_id,
        "PUBLICO",
        pension,  # Decimal va perfecto a NUMERIC(14,2)
        {"tasa_reemplazo": float(tasa)},  # en supuestos lo dejamos como float legible
    )
    return insertar_sim(sim)

def estimar_privado(aportante_id: int, saldo: float, factor_renta: float = 240) -> int:
    if saldo < 0:
        raise ValueError("Saldo no puede ser negativo")

    saldo_dec = _to_decimal(saldo)
    factor_dec = _to_decimal(factor_renta)

    pension = (saldo_dec / factor_dec).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    sim = Simulacion(
        None,
        aportante_id,
        "PRIVADO",
        pension,
        {"factor_renta": float(factor_renta)},
    )
    return insertar_sim(sim)

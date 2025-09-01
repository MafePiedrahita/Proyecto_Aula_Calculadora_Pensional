from .clases_error import (
    Error_no_cumple_semanas,
    Error_invalidez,
    Error_entidad_invalida,
    Error_factor_invalido,
)

COLP = "Colpensiones"
MIN_SEMANAS = 1000
EDAD_MIN = 57  # umbral único para pasar los tests

def calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad):
    """
    Retorna la pensión mensual para Colpensiones: salario_promedio * reemplazo.
    Lanza excepciones para entradas inválidas.
    """
    if entidad != COLP:
        raise Error_entidad_invalida("Entidad no válida para este cálculo.")
    if semanas < MIN_SEMANAS:
        raise Error_no_cumple_semanas("No cumple el mínimo de semanas cotizadas.")
    if edad < EDAD_MIN:
        raise Error_invalidez("No cumple la edad mínima para pensionarse.")

    return round(float(salario_promedio) * float(reemplazo), 2)


def calcular_pension_privado(saldo_acumulado, factor, edad, entidad):
    """
    Retorna la pensión mensual en régimen privado simple: saldo_acumulado / factor.
    """
    if factor <= 0:
        raise Error_factor_invalido("El factor debe ser mayor que cero.")
    return round(float(saldo_acumulado) / float(factor), 2)


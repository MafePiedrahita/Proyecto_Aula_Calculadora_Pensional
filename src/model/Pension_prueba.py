from .clases_error import Error_no_cumple_semanas, Error_invalidez, Error_entidad_invalida, Error_factor_invalido


def calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad):
    """Calcula la pensión mensual en Colpensiones"""

    entidades_validas = ["Colpensiones"]
    if entidad not in entidades_validas:
        raise Error_entidad_invalida("Entidad inválida")

    if semanas < 1000:
        raise Error_no_cumple_semanas("No cumple con el mínimo de semanas cotizadas")

    if edad < 50:
        raise Error_invalidez("Error por invalidez no válida")

    return salario_promedio * reemplazo


def calcular_pension_privado(saldo_acumulado, factor, edad, entidad):
    """Calcula la pensión mensual en un fondo privado"""

    entidades_validas = ["Protección", "Porvenir", "Colfondos", "Skandia"]
   
    if entidad not in entidades_validas:
        raise Error_entidad_invalida("Entidad inválida")

    if factor <= 0:
        raise Error_factor_invalido("Factor de cálculo inválido")

    if saldo_acumulado > 0:
        return round(saldo_acumulado / factor, 2)
    

    return "No tiene saldo suficiente"
       


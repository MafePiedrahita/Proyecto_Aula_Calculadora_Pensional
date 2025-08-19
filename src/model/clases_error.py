class Error_no_cumple_semanas(Exception):
     """Error cuando las semanas cotizadas no cumplen el minimo"""

class Error_invalidez_no_calificada(Exception):
     """Error cuando la invalidez no calificada, no cumple las semanas"""

def calcular_reemplazo_colpensiones(salario_promedio,  reemplazo, semanas, edad, entidad):
    """Calcula la pension mensual """
    if semanas >= 1000:
        raise Error_no_cumple_semanas("No cumple con el minimo de semanas cotizadas")
    
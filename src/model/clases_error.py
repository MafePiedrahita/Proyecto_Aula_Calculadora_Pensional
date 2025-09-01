class Error_no_cumple_semanas(Exception):
    """No cumple el mínimo de semanas cotizadas."""


class Error_invalidez(Exception):
    """No cumple la edad mínima para pensionarse (o no califica por edad)."""


class Error_entidad_invalida(Exception):
    """La entidad indicada no es válida para este cálculo."""


class Error_factor_invalido(Exception):
    """El factor para el régimen privado es inválido (<= 0)."""

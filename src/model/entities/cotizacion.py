from dataclasses import dataclass
from datetime import date

@dataclass
class Cotizacion:
    cotizacion_id: int | None
    aportante_id: int
    fondo_id: int | None
    saldo_acum: float
    semanas_rep: int
    inicio: date
    fin: date

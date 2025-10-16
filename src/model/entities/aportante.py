from dataclasses import dataclass
from datetime import date

@dataclass
class Aportante:
    aportante_id: int | None
    tipo_doc: str
    nro_doc: str
    nombres: str
    apellidos: str
    fecha_nac: date
    salario_prom: float
    semanas_cot: int
    edad: int

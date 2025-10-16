from dataclasses import dataclass
from datetime import datetime

@dataclass
class Simulacion:
    simulacion_id: int | None
    aportante_id: int
    pilar: str             # 'PUBLICO' | 'PRIVADO'
    pension_mens: float
    supuestos: dict
    creado_en: datetime | None = None

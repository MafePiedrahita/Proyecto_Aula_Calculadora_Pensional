from typing import List
from psycopg2.extras import Json
from src.model.conexion_db import db_cursor
from src.model.entities.simulacion import Simulacion

# CREATE (insertar simulación)
def insertar(sim: Simulacion) -> int:
    """
    Inserta una simulación. 'supuestos' se guarda como JSONB.
    """
    sql = """
    INSERT INTO simulacion (aportante_id, pilar, pension_mens, supuestos)
    VALUES (%s, %s, %s, %s)
    RETURNING simulacion_id;
    """
    with db_cursor() as (conn, cur):
        cur.execute(sql, (sim.aportante_id, sim.pilar, sim.pension_mens, Json(sim.supuestos)))
        new_id = cur.fetchone()[0]
    return new_id

# READ (por id)
def buscar_por_id(simulacion_id: int) -> Simulacion | None:
    sql = """
    SELECT simulacion_id, aportante_id, pilar, pension_mens, supuestos, creado_en
    FROM simulacion
    WHERE simulacion_id = %s;
    """
    with db_cursor(dict_cursor=True) as (conn, cur):
        cur.execute(sql, (simulacion_id,))
        row = cur.fetchone()
        if not row:
            return None
        # Map a la Entity (creado_en puede venir como datetime)
        return Simulacion(**row)

# READ (todas por aportante)
def listar_por_aportante(aportante_id: int) -> List[Simulacion]:
    sql = """
    SELECT simulacion_id, aportante_id, pilar, pension_mens, supuestos, creado_en
    FROM simulacion
    WHERE aportante_id = %s
    ORDER BY creado_en DESC;
    """
    with db_cursor(dict_cursor=True) as (conn, cur):
        cur.execute(sql, (aportante_id,))
        rows = cur.fetchall() or []
        return [Simulacion(**r) for r in rows]

# Opcional: filtros por pilar
def listar_por_aportante_y_pilar(aportante_id: int, pilar: str) -> List[Simulacion]:
    sql = """
    SELECT simulacion_id, aportante_id, pilar, pension_mens, supuestos, creado_en
    FROM simulacion
    WHERE aportante_id = %s AND pilar = %s
    ORDER BY creado_en DESC;
    """
    with db_cursor(dict_cursor=True) as (conn, cur):
        cur.execute(sql, (aportante_id, pilar))
        rows = cur.fetchall() or []
        return [Simulacion(**r) for r in rows]

# DELETE (para limpiar pruebas / permitir repetir simulaciones)
def eliminar(simulacion_id: int) -> int:
    sql = "DELETE FROM simulacion WHERE simulacion_id = %s;"
    with db_cursor() as (conn, cur):
        cur.execute(sql, (simulacion_id,))
        return cur.rowcount

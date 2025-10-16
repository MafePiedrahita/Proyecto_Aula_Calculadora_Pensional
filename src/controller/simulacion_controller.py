# src/controller/simulacion_controller.py
from typing import List
from psycopg2.extras import Json
from src.model.conexion_db import db_cursor
from src.model.entities.simulacion import Simulacion

def insertar(sim: Simulacion) -> int:
    sql = """
    INSERT INTO simulacion (aportante_id, pilar, pension_mens, supuestos)
    VALUES (%s, %s, %s, %s)
    RETURNING simulacion_id;
    """
    with db_cursor() as (conn, cur):
        cur.execute(sql, (sim.aportante_id, sim.pilar, sim.pension_mens, Json(sim.supuestos)))
        return cur.fetchone()["simulacion_id"]

def buscar_por_id(simulacion_id: int) -> Simulacion | None:
    sql = """
    SELECT simulacion_id, aportante_id, pilar, pension_mens, supuestos, creado_en
    FROM simulacion WHERE simulacion_id = %s;
    """
    with db_cursor() as (conn, cur):
        cur.execute(sql, (simulacion_id,))
        row = cur.fetchone()
        return Simulacion(**row) if row else None

def listar_por_aportante(aportante_id: int) -> List[Simulacion]:
    sql = """
    SELECT simulacion_id, aportante_id, pilar, pension_mens, supuestos, creado_en
    FROM simulacion WHERE aportante_id = %s
    ORDER BY creado_en DESC;
    """
    with db_cursor() as (conn, cur):
        cur.execute(sql, (aportante_id,))
        rows = cur.fetchall() or []
        return [Simulacion(**r) for r in rows]

def listar_por_aportante_y_pilar(aportante_id: int, pilar: str) -> List[Simulacion]:
    sql = """
    SELECT simulacion_id, aportante_id, pilar, pension_mens, supuestos, creado_en
    FROM simulacion WHERE aportante_id = %s AND pilar = %s
    ORDER BY creado_en DESC;
    """
    with db_cursor() as (conn, cur):
        cur.execute(sql, (aportante_id, pilar))
        rows = cur.fetchall() or []
        return [Simulacion(**r) for r in rows]

def eliminar(simulacion_id: int) -> int:
    with db_cursor() as (conn, cur):
        cur.execute("DELETE FROM simulacion WHERE simulacion_id = %s;", (simulacion_id,))
        return cur.rowcount

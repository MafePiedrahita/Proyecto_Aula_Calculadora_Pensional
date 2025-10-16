# src/controller/cotizacion_controller.py
from typing import List
from src.model.conexion_db import db_cursor
from src.model.entities.cotizacion import Cotizacion

def crear(ctz: Cotizacion) -> int:
    sql = """
    INSERT INTO cotizacion (aportante_id, fondo_id, saldo_acum, semanas_rep, periodo)
    VALUES (%s, %s, %s, %s, daterange(%s, %s, '[]'))
    RETURNING cotizacion_id;
    """
    with db_cursor() as (conn, cur):
        cur.execute(sql, (ctz.aportante_id, ctz.fondo_id, ctz.saldo_acum,
                          ctz.semanas_rep, ctz.inicio, ctz.fin))
        return cur.fetchone()["cotizacion_id"]

def buscar_por_id(cotizacion_id: int) -> Cotizacion | None:
    sql = """
    SELECT
      cotizacion_id, aportante_id, fondo_id, saldo_acum, semanas_rep,
      lower(periodo) AS inicio, upper(periodo) AS fin
    FROM cotizacion WHERE cotizacion_id = %s;
    """
    with db_cursor() as (conn, cur):
        cur.execute(sql, (cotizacion_id,))
        row = cur.fetchone()
        return Cotizacion(**row) if row else None

def listar_por_aportante(aportante_id: int) -> List[Cotizacion]:
    sql = """
    SELECT
      cotizacion_id, aportante_id, fondo_id, saldo_acum, semanas_rep,
      lower(periodo) AS inicio, upper(periodo) AS fin
    FROM cotizacion
    WHERE aportante_id = %s
    ORDER BY inicio;
    """
    with db_cursor() as (conn, cur):
        cur.execute(sql, (aportante_id,))
        rows = cur.fetchall() or []
        return [Cotizacion(**r) for r in rows]

def actualizar(ctz: Cotizacion) -> int:
    if ctz.cotizacion_id is None:
        raise ValueError("cotizacion_id es obligatorio para actualizar")
    sql = """
    UPDATE cotizacion
    SET fondo_id = %s,
        saldo_acum = %s,
        semanas_rep = %s,
        periodo = daterange(%s, %s, '[]')
    WHERE cotizacion_id = %s;
    """
    with db_cursor() as (conn, cur):
        cur.execute(sql, (ctz.fondo_id, ctz.saldo_acum, ctz.semanas_rep,
                          ctz.inicio, ctz.fin, ctz.cotizacion_id))
        return cur.rowcount

def eliminar(cotizacion_id: int) -> int:
    with db_cursor() as (conn, cur):
        cur.execute("DELETE FROM cotizacion WHERE cotizacion_id = %s;", (cotizacion_id,))
        return cur.rowcount

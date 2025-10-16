from typing import List
from psycopg2.extras import RealDictCursor
from src.model.conexion_db import db_cursor
from src.model.entities.cotizacion import Cotizacion

# CREATE
def crear(ctz: Cotizacion) -> int:
    """
    Inserta una cotización.
    Mapea (inicio, fin) -> DATERANGE inclusivo en ambos lados '[]'.
    """
    sql = """
    INSERT INTO cotizacion (aportante_id, fondo_id, saldo_acum, semanas_rep, periodo)
    VALUES (%s, %s, %s, %s, daterange(%s, %s, '[]'))
    RETURNING cotizacion_id;
    """
    with db_cursor() as (conn, cur):
        cur.execute(sql, (ctz.aportante_id, ctz.fondo_id, ctz.saldo_acum,
                          ctz.semanas_rep, ctz.inicio, ctz.fin))
        new_id = cur.fetchone()[0]
    return new_id

# READ (por id)
def buscar_por_id(cotizacion_id: int) -> Cotizacion | None:
    sql = """
    SELECT
      cotizacion_id, aportante_id, fondo_id, saldo_acum, semanas_rep,
      lower(periodo) AS inicio, upper(periodo) AS fin
    FROM cotizacion
    WHERE cotizacion_id = %s;
    """
    with db_cursor(dict_cursor=True) as (conn, cur):
        cur.execute(sql, (cotizacion_id,))
        row = cur.fetchone()
        return Cotizacion(**row) if row else None

# READ (todas por aportante)
def listar_por_aportante(aportante_id: int) -> List[Cotizacion]:
    sql = """
    SELECT
      cotizacion_id, aportante_id, fondo_id, saldo_acum, semanas_rep,
      lower(periodo) AS inicio, upper(periodo) AS fin
    FROM cotizacion
    WHERE aportante_id = %s
    ORDER BY inicio;
    """
    with db_cursor(dict_cursor=True) as (conn, cur):
        cur.execute(sql, (aportante_id,))
        rows = cur.fetchall() or []
        return [Cotizacion(**r) for r in rows]

# UPDATE (todo el registro)
def actualizar(ctz: Cotizacion) -> int:
    """
    Actualiza fondo_id, saldo_acum, semanas_rep y periodo.
    Requiere ctz.cotizacion_id.
    """
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

# DELETE
def eliminar(cotizacion_id: int) -> int:
    sql = "DELETE FROM cotizacion WHERE cotizacion_id = %s;"
    with db_cursor() as (conn, cur):
        cur.execute(sql, (cotizacion_id,))
        return cur.rowcount

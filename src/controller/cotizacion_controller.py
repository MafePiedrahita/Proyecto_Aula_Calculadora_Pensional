from src.model.conexion_db import db_cursor
from src.controller.aportante_controller import buscar_por_id
from src.model.entities.cotizacion import Cotizacion


def _row_to_cotizacion(row) -> Cotizacion:
    """
    BD -> Entidad
    BD: cotizacion_id, aportante_id, fondo_id, saldo_acum, semanas_rep, inicio, fin
    Entidad: cotizacion_id, aportante_id, fondo_id, saldo_acum, semanas_rep, inicio, fin
    (misma nomenclatura para evitar confusiones)
    """
    return Cotizacion(
        row["cotizacion_id"],
        row["aportante_id"],
        row.get("fondo_id"),
        row["saldo_acum"],
        row["semanas_rep"],
        row["inicio"],
        row["fin"],
    )


def crear(c: Cotizacion) -> int:
    """
    Inserta una cotización usando las columnas reales de la tabla:
    saldo_acum, semanas_rep, inicio, fin
    """
    if c.inicio > c.fin:
        raise ValueError("Rango de fechas inválido (inicio > fin)")
    if not buscar_por_id(c.aportante_id):
        raise ValueError("Aportante no existe")

    sql = """
    INSERT INTO cotizacion (aportante_id, fondo_id, saldo_acum, semanas_rep, inicio, fin)
    VALUES (%s, %s, %s, %s, %s, %s)
    RETURNING cotizacion_id;
    """
    params = (
        c.aportante_id,
        c.fondo_id,
        c.saldo_acum,
        c.semanas_rep,
        c.inicio,
        c.fin,
    )
    with db_cursor() as (conn, cur):
        cur.execute(sql, params)
        return cur.fetchone()["cotizacion_id"]


def listar_por_aportante(aportante_id: int) -> list[Cotizacion]:
    sql = """
    SELECT cotizacion_id, aportante_id, fondo_id, saldo_acum, semanas_rep, inicio, fin
      FROM cotizacion
     WHERE aportante_id = %s
     ORDER BY cotizacion_id;
    """
    with db_cursor() as (conn, cur):
        cur.execute(sql, (aportante_id,))
        rows = cur.fetchall()
        return [_row_to_cotizacion(r) for r in rows]


def actualizar(c: Cotizacion) -> int:
    if c.inicio > c.fin:
        raise ValueError("Rango de fechas inválido (inicio > fin)")

    sql = """
    UPDATE cotizacion
       SET fondo_id   = %s,
           saldo_acum = %s,
           semanas_rep= %s,
           inicio     = %s,
           fin        = %s
     WHERE cotizacion_id = %s
       AND aportante_id  = %s;
    """
    params = (
        c.fondo_id,
        c.saldo_acum,
        c.semanas_rep,
        c.inicio,
        c.fin,
        c.cotizacion_id,
        c.aportante_id,
    )
    with db_cursor() as (conn, cur):
        cur.execute(sql, params)
        return cur.rowcount


def eliminar(cotizacion_id: int, aportante_id: int) -> int:
    sql = "DELETE FROM cotizacion WHERE cotizacion_id = %s AND aportante_id = %s;"
    with db_cursor() as (conn, cur):
        cur.execute(sql, (cotizacion_id, aportante_id))
        return cur.rowcount

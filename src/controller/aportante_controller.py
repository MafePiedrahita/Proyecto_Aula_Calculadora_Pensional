# src/controller/aportante_controller.py
from src.model.conexion_db import db_cursor
from src.model.entities.aportante import Aportante

def crear(ap: Aportante) -> int:
    sql = """
    INSERT INTO aportante (tipo_doc, nro_doc, nombres, apellidos, fecha_nac,
                           salario_prom, semanas_cot, edad)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    RETURNING aportante_id;
    """
    with db_cursor() as (conn, cur):
        cur.execute(sql, (ap.tipo_doc, ap.nro_doc, ap.nombres, ap.apellidos,
                          ap.fecha_nac, ap.salario_prom, ap.semanas_cot, ap.edad))
        return cur.fetchone()["aportante_id"]

def buscar_por_id(aportante_id: int) -> Aportante | None:
    sql = "SELECT * FROM aportante WHERE aportante_id = %s;"
    with db_cursor() as (conn, cur):
        cur.execute(sql, (aportante_id,))
        row = cur.fetchone()
        return Aportante(**row) if row else None

def actualizar_salario(aportante_id: int, nuevo_salario: float) -> int:
    sql = "UPDATE aportante SET salario_prom = %s WHERE aportante_id = %s;"
    with db_cursor() as (conn, cur):
        cur.execute(sql, (nuevo_salario, aportante_id))
        return cur.rowcount

def eliminar(aportante_id: int) -> int:
    sql = "DELETE FROM aportante WHERE aportante_id = %s;"
    with db_cursor() as (conn, cur):
        cur.execute(sql, (aportante_id,))
        return cur.rowcount
    
def buscar_por_nro_doc(nro_doc: str) -> Aportante | None:
    """
    Retorna el aportante con el número de documento dado, o None si no existe.
    """
    sql = "SELECT * FROM aportante WHERE nro_doc = %s;"
    with db_cursor() as (conn, cur):
        cur.execute(sql, (nro_doc,))
        row = cur.fetchone()
        return Aportante(**row) if row else None
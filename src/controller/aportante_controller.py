from psycopg2.extras import RealDictCursor
from src.model.conexion_db import get_connection, put_connection
from src.model.entities.aportante import Aportante

def crear(ap: Aportante) -> int:
    sql = """
      INSERT INTO aportante (tipo_doc, nro_doc, nombres, apellidos, fecha_nac,
                             salario_prom, semanas_cot, edad)
      VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
      RETURNING aportante_id;
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (ap.tipo_doc, ap.nro_doc, ap.nombres, ap.apellidos,
                              ap.fecha_nac, ap.salario_prom, ap.semanas_cot, ap.edad))
            new_id = cur.fetchone()[0]
            conn.commit()
            return new_id
    except Exception:
        conn.rollback()
        raise
    finally:
        put_connection(conn)

def buscar_por_id(aportante_id: int) -> Aportante | None:
    sql = "SELECT * FROM aportante WHERE aportante_id = %s;"
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, (aportante_id,))
            row = cur.fetchone()
            if not row: return None
            return Aportante(**row)
    finally:
        put_connection(conn)

def actualizar_salario(aportante_id: int, nuevo_salario: float) -> int:
    sql = "UPDATE aportante SET salario_prom = %s WHERE aportante_id = %s;"
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (nuevo_salario, aportante_id))
            conn.commit()
            return cur.rowcount
    except Exception:
        conn.rollback()
        raise
    finally:
        put_connection(conn)

def eliminar(aportante_id: int) -> int:
    sql = "DELETE FROM aportante WHERE aportante_id = %s;"
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (aportante_id,))
            conn.commit()
            return cur.rowcount
    except Exception:
        conn.rollback()
        raise
    finally:
        put_connection(conn)

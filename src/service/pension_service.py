from typing import List, Dict, Optional
from src.model.conexion_db import db_cursor


# 🔹 Ajusta estos nombres si tu tabla/columnas tienen otros nombres en 01_schema.sql
TABLE_NAME = "aportantes"              # nombre de la tabla
COL_NOMBRE = "nombre"
COL_DOCUMENTO = "documento"
COL_SALARIO = "salario_promedio"


def insertar_aportante(nombre: str, documento: str, salario: float) -> None:
    """
    Inserta un aportante nuevo.
    Si el documento ya existe, actualiza nombre y salario (UPSERT).
    """
    with db_cursor() as (conn, cur):
        cur.execute(
            f"""
            INSERT INTO {TABLE_NAME} ({COL_NOMBRE}, {COL_DOCUMENTO}, {COL_SALARIO})
            VALUES (%s, %s, %s)
            ON CONFLICT ({COL_DOCUMENTO}) DO UPDATE
            SET {COL_NOMBRE} = EXCLUDED.{COL_NOMBRE},
                {COL_SALARIO} = EXCLUDED.{COL_SALARIO};
            """,
            (nombre, documento, salario),
        )


def buscar_aportante_por_documento(documento: str) -> Optional[Dict]:
    """
    Busca un aportante por documento.
    Retorna un diccionario o None si no existe.
    """
    with db_cursor() as (conn, cur):
        cur.execute(
            f"""
            SELECT {COL_NOMBRE}, {COL_DOCUMENTO}, {COL_SALARIO}
            FROM {TABLE_NAME}
            WHERE {COL_DOCUMENTO} = %s;
            """,
            (documento,),
        )
        row = cur.fetchone()

    if not row:
        return None

    return {
        "nombre": row[0],
        "documento": row[1],
        "salario": float(row[2]) if row[2] is not None else None,
    }


def listar_aportantes() -> List[Dict]:
    """
    Lista todos los aportantes.
    """
    with db_cursor() as (conn, cur):
        cur.execute(
            f"""
            SELECT {COL_NOMBRE}, {COL_DOCUMENTO}, {COL_SALARIO}
            FROM {TABLE_NAME}
            ORDER BY {COL_NOMBRE};
            """
        )
        rows = cur.fetchall()

    resultado = []
    for row in rows:
        resultado.append(
            {
                "nombre": row[0],
                "documento": row[1],
                "salario": float(row[2]) if row[2] is not None else None,
            }
        )
    return resultado

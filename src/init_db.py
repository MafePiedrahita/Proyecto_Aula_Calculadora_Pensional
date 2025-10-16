from src.model.conexion_db import db_cursor

def apply_schema(path_sql: str = "sql/01_schema.sql"):
    with db_cursor() as (conn, cur):
        with open(path_sql, "r", encoding="utf-8") as f:
            cur.execute(f.read())
    print("✔ Esquema aplicado correctamente.")

if __name__ == "__main__":
    apply_schema()

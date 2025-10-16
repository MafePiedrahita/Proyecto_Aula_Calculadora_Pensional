import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from src.secret_config import DB_CONFIG


@contextmanager
def db_cursor():
    """Context manager para abrir conexión y cursor automáticamente."""
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        yield conn, cur
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

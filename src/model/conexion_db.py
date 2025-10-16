import psycopg2
from psycopg2 import pool
from src.secret_config import DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT

_pool = None

def _get_pool():
    global _pool
    if _pool is None:
        _pool = psycopg2.pool.SimpleConnectionPool(
            1, 5,
            dbname=DB_NAME, user=DB_USER, password=DB_PASS,
            host=DB_HOST, port=DB_PORT
        )
    return _pool

def get_connection():
    return _get_pool().getconn()

def put_connection(conn):
    _get_pool().putconn(conn)


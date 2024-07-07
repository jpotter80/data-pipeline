import os
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_batch
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection parameters
db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432')
}

def execute_sql(query, params=None):
    conn = psycopg2.connect(**db_params)
    try:
        with conn.cursor() as cur:
            if params:
                if isinstance(params[0], tuple):
                    execute_batch(cur, query, params)
                else:
                    cur.execute(query, params)
            else:
                cur.execute(query)
            conn.commit()
            if cur.description:
                return cur.fetchall()
    finally:
        conn.close()

def get_db_info():
    return {
        'dbname': db_params['dbname'],
        'user': db_params['user'],
        'host': db_params['host'],
        'port': db_params['port']
    }
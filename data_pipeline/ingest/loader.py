import os
import pandas as pd
from typing import List, Dict
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

load_dotenv()

class CSVLoader:
    def __init__(self, dataset_dir: str = 'dataset'):
        self.dataset_dir = dataset_dir

    def list_csv_files(self) -> List[str]:
        return [f for f in os.listdir(self.dataset_dir) if f.endswith('.csv')]

    def get_database_name(self) -> str:
        csv_files = self.list_csv_files()
        if not csv_files:
            raise ValueError("No CSV files found in the dataset directory.")
        return os.path.splitext(csv_files[0])[0]

    def load_csv(self, filename: str) -> pd.DataFrame:
        filepath = os.path.join(self.dataset_dir, filename)
        return pd.read_csv(filepath)

    def analyze_csv_structure(self, df: pd.DataFrame) -> Dict:
        return {
            'columns': df.columns.tolist(),
            'dtypes': df.dtypes.to_dict(),
            'sample_data': df.head().to_dict(),
            'null_counts': df.isnull().sum().to_dict(),
            'row_count': len(df)
        }

    def process_all_csv(self) -> List[Dict]:
        results = []
        for csv_file in self.list_csv_files():
            df = self.load_csv(csv_file)
            analysis = self.analyze_csv_structure(df)
            results.append({
                'filename': csv_file,
                'analysis': analysis
            })
        return results

class DBLoader:
    def __init__(self, db_name: str):
        self.conn_params = {
            'dbname': db_name,
            'user': os.getenv('DB_USER', 'postgres'),
            'password': os.getenv('DB_PASS'),
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': os.getenv('DB_PORT', '5432')
        }

    def database_exists(self) -> bool:
        """Check if the database already exists."""
        conn_params = self.conn_params.copy()
        conn_params['dbname'] = 'postgres'
        conn = psycopg2.connect(**conn_params)
        conn.autocommit = True
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (self.conn_params['dbname'],))
                return cur.fetchone() is not None
        finally:
            conn.close()

    def create_database(self):
        if self.database_exists():
            print(f"Database {self.conn_params['dbname']} already exists.")
            return

        conn_params = self.conn_params.copy()
        conn_params['dbname'] = 'postgres'
        conn = psycopg2.connect(**conn_params)
        conn.autocommit = True
        try:
            with conn.cursor() as cur:
                cur.execute(f"CREATE DATABASE {self.conn_params['dbname']}")
            print(f"Database {self.conn_params['dbname']} created successfully.")
        finally:
            conn.close()

    def table_exists(self, table_name: str) -> bool:
        """Check if a table already exists in the database."""
        conn = psycopg2.connect(**self.conn_params)
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT 1 FROM information_schema.tables 
                    WHERE table_name = %s
                """, (table_name,))
                return cur.fetchone() is not None
        finally:
            conn.close()

    def create_table(self, table_name: str, df: pd.DataFrame):
        if self.table_exists(table_name):
            print(f"Table {table_name} already exists.")
            return

        conn = psycopg2.connect(**self.conn_params)
        try:
            with conn.cursor() as cur:
                columns = []
                for col, dtype in df.dtypes.items():
                    if dtype == 'object':
                        col_type = 'TEXT'
                    elif dtype == 'int64':
                        col_type = 'INTEGER'
                    elif dtype == 'float64':
                        col_type = 'FLOAT'
                    else:
                        col_type = 'TEXT'
                    columns.append(f'"{col}" {col_type}')
                
                create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id SERIAL PRIMARY KEY,
                    {', '.join(columns)}
                )
                """
                cur.execute(create_table_query)
            conn.commit()
            print(f"Table {table_name} created successfully.")
        finally:
            conn.close()

    def table_is_empty(self, table_name: str) -> bool:
        """Check if a table is empty."""
        conn = psycopg2.connect(**self.conn_params)
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT 1 FROM {table_name} LIMIT 1")
                return cur.fetchone() is None
        finally:
            conn.close()

    def insert_data(self, table_name: str, df: pd.DataFrame):
        if not self.table_is_empty(table_name):
            print(f"Table {table_name} already contains data. Skipping insertion.")
            return

        conn = psycopg2.connect(**self.conn_params)
        try:
            with conn.cursor() as cur:
                columns = [f'"{col}"' for col in df.columns]
                values = [tuple(row) for row in df.values]
                insert_query = f"""
                INSERT INTO {table_name} ({', '.join(columns)})
                VALUES %s
                """
                execute_values(cur, insert_query, values)
            conn.commit()
            print(f"Data inserted into {table_name} successfully.")
        finally:
            conn.close()
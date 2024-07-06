"""
Module for loading CSV files and managing database operations.
"""

import logging
from typing import List, Optional, Dict
from pathlib import Path
import io
import pandas as pd
import aiofiles
import asyncpg

logger = logging.getLogger(__name__)

class CSVLoader:
    """Class for loading and processing CSV files."""

    def __init__(self, data_dir: Path):
        """
        Initialize the CSVLoader.

        Args:
            data_dir (Path): Directory containing CSV files.
        """
        self.data_dir = data_dir

    def get_csv_files(self) -> List[str]:
        """
        Get a list of CSV files in the data directory.

        Returns:
            List[str]: List of CSV filenames.
        """
        return [f.name for f in self.data_dir.glob('*.csv')]

    async def load_csv(self, filename: str) -> Optional[pd.DataFrame]:
        """
        Load a CSV file asynchronously.

        Args:
            filename (str): Name of the CSV file to load.

        Returns:
            Optional[pd.DataFrame]: Loaded DataFrame or None if loading fails.
        """
        file_path = self.data_dir / filename
        try:
            async with aiofiles.open(file_path, mode='r') as f:
                content = await f.read()
            df = pd.read_csv(io.StringIO(content))
            logger.info(f"Successfully loaded {filename}")
            return df
        except (IOError, pd.errors.EmptyDataError) as e:
            logger.error(f"Error loading {filename}: {str(e)}")
            return None

class DBLoader:
    """Class for database operations."""

    def __init__(self, db_config: dict):
        """
        Initialize the DBLoader.

        Args:
            db_config (dict): Database configuration parameters.
        """
        self.db_config = db_config

    async def get_or_create_database(self, csv_files: List[str]) -> Optional[str]:
        """
        Get an existing database or create a new one.

        Args:
            csv_files (List[str]): List of CSV filenames.

        Returns:
            Optional[str]: Database name or None if operation fails.
        """
        try:
            conn = await asyncpg.connect(**self.db_config, database='postgres')
            try:
                for csv_file in csv_files:
                    db_name = Path(csv_file).stem.lower()
                    exists = await conn.fetchval(
                        "SELECT 1 FROM pg_database WHERE datname = $1", db_name
                    )
                    if exists:
                        logger.info(f"Database {db_name} already exists.")
                        return db_name
                
                # If no matching database found, create one with the first CSV file name
                db_name = Path(csv_files[0]).stem.lower()
                await conn.execute(f"CREATE DATABASE {db_name}")
                logger.info(f"Database {db_name} created successfully.")
                return db_name
            finally:
                await conn.close()
        except asyncpg.PostgresError as e:
            logger.error(f"Error checking/creating database: {e}")
            return None

    async def create_table(self, db_name: str, table_name: str, df: pd.DataFrame, sql_data_types: Dict[str, str]):
        """
        Create a table in the database.

        Args:
            db_name (str): Name of the database.
            table_name (str): Name of the table to create.
            df (pd.DataFrame): DataFrame containing the data.
            sql_data_types (Dict[str, str]): Mapping of column names to SQL data types.
        """
        try:
            conn = await asyncpg.connect(**self.db_config, database=db_name)
            try:
                columns = [f'"{col}" {sql_data_types[col]}' for col in df.columns]
                create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id SERIAL PRIMARY KEY,
                    {', '.join(columns)}
                )
                """
                await conn.execute(create_table_query)
                logger.info(f"Table {table_name} created successfully in database {db_name}.")
            finally:
                await conn.close()
        except asyncpg.PostgresError as e:
            logger.error(f"Error creating table: {e}")

    async def insert_data(self, db_name: str, table_name: str, df: pd.DataFrame, sql_data_types: Dict[str, str]):
        """
        Insert data into the database table.

        Args:
            db_name (str): Name of the database.
            table_name (str): Name of the table to insert data into.
            df (pd.DataFrame): DataFrame containing the data to insert.
            sql_data_types (Dict[str, str]): Mapping of column names to SQL data types.
        """
        try:
            conn = await asyncpg.connect(**self.db_config, database=db_name)
            try:
                # Check if table is empty
                count = await conn.fetchval(f"SELECT COUNT(*) FROM {table_name}")
                if count > 0:
                    logger.info(f"Table {table_name} already contains data. Skipping insertion.")
                    return

                # Prepare data for insertion
                columns = [f'"{col}"' for col in df.columns]
                values = [tuple(row) for _, row in df.iterrows()]
                
                # Construct the INSERT query
                insert_query = f"""
                INSERT INTO {table_name} ({', '.join(columns)})
                VALUES ({', '.join(['$' + str(i+1) for i in range(len(columns))])})
                """
                
                # Execute the INSERT query for all rows
                await conn.executemany(insert_query, values)
                logger.info(f"Data inserted into {table_name} in database {db_name} successfully.")
            finally:
                await conn.close()
        except asyncpg.PostgresError as e:
            logger.error(f"Error inserting data: {e}")
"""
PostgresSQL adapter
"""
from collections.abc import Callable
import psycopg as db

from utils.logger import logger


def load_database_engine(database_engine: Callable[[str, str, list[dict]], None]
) -> Callable[[str, str, list[dict]], None]:
    """
    Higher-order function to load data into a database using the provided database engine function.

    Args:
        database_engine: A function that performs the actual DB insert.
        connection: A database connection string.
        query: SQL insert query to use.

    Returns:
        A function that accepts data and executes the insert using the database engine.
    """
    def loader(connection: str, query: str, data: list[dict]) -> None:
        try:
            logger.info("Attempting to load data to the database...")
            database_engine(connection, query, data)
            logger.info("Data successfully loaded.")
        except Exception as error:
            logger.error(f"Failed to load data: {error}")
    return loader

def insert_into_postgresql(connection_info: str, query: str, records: list[dict]) -> None:
    """
    Connects to a PostgreSQL database and inserts a list of records via a query

    Args:
        connection_info (str): The database connection string.
        query (str): The SQL query.
        records (list[dict]): The records to insert.

    Returns:
        None
    """
    with db.connect(conninfo=connection_info) as connection:
        logger.info(f"Established db connection: {connection_info}")
        for record in records:
            with connection.cursor() as running_cursor:
                try:
                    running_cursor.execute(query, record)
                except db.Error as error:
                    logger.error(error)

def insert_into_mysql(connection_info: str, query: str, records: list[dict]) -> None:
    """
    Connects to a MySQL database and inserts a list of records via a query

    Args:
        connection_info (str): The database connection string.
        query (str): The SQL query.
        records (list[dict]): The records to insert.

    Returns:
        None
    """
    pass

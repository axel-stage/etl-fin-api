"""
PostgresSQL adapter
"""
import psycopg as db

from utils.logger import logger


def insert_records(connection_info: str, query: str, records: list[dict]) -> None:
    """
    Connects to a database and inserts a list of records via a query

    Args:
        connection_info (str): The database connection.
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
                except db.Error as err:
                    logger.error(err)

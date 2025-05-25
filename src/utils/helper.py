"""
module is a container for helper functions
"""

def create_api_endpoint(
    base_url: str,
    function: str,
    symbol: str,
    api_key: str) -> str:
    """
    Creates an API endpoint string to request a resource.

    Args:
        base_url (str): The static part of the API URL resource.
        function (str): The function API parameter.
        symbol (str): The function API parameter.
        api_key (str): The API key parameter.

    Returns:
        str: API endpoint string
    """
    return f"{base_url}query?function={function}&symbol={symbol}&apikey={api_key}"


def insert_symbol(symbol: str, fields: list[dict]) -> None:
    """
    Inserts the symbol into a list of list of dictionary's.

    Args:
        symbol (str): The symbol value.
        fields (list[dict]): The list of dictionary's.

    Returns:
        None
    """
    for field in fields:
        #field["symbol"] = symbol
        field.symbol = symbol


def create_database_connection_info(
    user: str,
    password: str,
    host: str,
    port: str,
    database: str,
    dbms: str = "postgresql") -> str:
    """
    Creates an client connection string, used to connect to a PostgreSQL database server.

    Args:
        user (str): The database user.
        password (str): The database password.
        host (str): The host name or IPv4 address.
        port (str): The database port.
        database (str): The database name.
        dbms (str): The database management system.

    Returns:
        str: client connection string
    """
    return f"{dbms}://{user}:{password}@{host}:{port}/{database}"

"""
module is a container for helper functions
"""

def create_api_endpoint(
    base_url: str,
    function: str,
    symbol: str,
    api_key: str) -> str:
    """
    Creates the string to the corresponding API endpoint to request a resource.

    Args:
        base_url (str): The static part of the API URL resource.
        function (str): The function API parameter.
        symbol (str): The function API parameter.
        api_key (str): The API key parameter.

    Returns:
        str: Concatenated API endpoint string
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
        field["symbol"] = symbol

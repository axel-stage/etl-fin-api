"""
Create an api client based on requests lib.

Functions:
    fetch_api_data(url: str)
"""

import requests
from utils.logger import logger


def fetch_api_data(url: str) -> dict:
    """
    Fetches data from an API and returns the parsed response.

    Args:
        url (str): The URL of the requested resource.

    Returns:
        dict: The parsed response object.
    """
    logger.info(f"Try to fetch data from API url: {url}")
    response = requests.get(url)
    logger.info(response.raise_for_status())
    return response.json()

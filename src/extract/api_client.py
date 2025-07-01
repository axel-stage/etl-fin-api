"""
Api client based on requests module.

Functions:
    fetch_api_data(url: str)
"""

import requests
from utils.logger import logger


def fetch_api_data(url: str) -> dict[str, str | int] | None:
    """
    Pure function to fetch data from a URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        dict | None: The JSON response or None if failed.
    """

    try:
        logger.info(f"Fetching data from URL: {url}")
        response = requests.get(url)
        logger.info(response.raise_for_status())
        return response.json()
    except requests.RequestException:
        logger.exception(f"Error fetching data from {url}")
        return None

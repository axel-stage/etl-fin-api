"""
main module
"""
from config import settings

from extract.api_client import fetch_api_data
from transform.schema_alpha_vantage import Company, IncomeStatement, BalanceSheet, CashFlow

from utils.logger import logger
from utils.helper import create_api_endpoint, insert_symbol_value

def etl_company(symbol: str) -> None:
    # extract
    url = create_api_endpoint(settings.BASE_URL, "OVERVIEW", symbol, settings.API_KEY)
    api_data = fetch_api_data(url)
    # transform
    company = Company.model_validate(api_data)
    clean_company = company.model_dump()
    records = [clean_company]
    print(records)

def main():
    """Data Pipeline entrypoint"""

    SYMBOL: str = "AMZN"

    etl_company(SYMBOL)

if __name__ == "__main__":
    main()

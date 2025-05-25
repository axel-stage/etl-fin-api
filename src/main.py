"""
main module
"""
from config import settings
from extract.api_client import fetch_api_data
from transform.schema_alpha_vantage import Company, IncomeStatement, BalanceSheet, CashFlow
from load.postgres_loader import insert_records
from load.postgres_query import PostgresQuery
from utils.logger import logger
from utils.helper import create_api_endpoint, insert_symbol, create_database_connection_info

def extract_transform_load(
        symbol: str,
        data_type: str,
        schema: Company | IncomeStatement | BalanceSheet | CashFlow,
        database_connection_info: str,
        query: str
    ) -> None:
    # extract
    endpoint = create_api_endpoint(settings.BASE_URL, data_type, symbol, settings.API_KEY)
    api_data = fetch_api_data(endpoint)
    # transform
    validated_data = schema.model_validate(api_data)
    if data_type != "OVERVIEW":
        insert_symbol(symbol, validated_data.data)
    clean_data = validated_data.model_dump()
    if data_type == "OVERVIEW":
        records = [clean_data]
    else:
        records = clean_data.get("data")
    # load
    insert_records(database_connection_info, query, records)

def main():
    """Data Pipeline entrypoint"""

    #SYMBOL: str = "AMZN"
    #SYMBOL: str = "MSFT"
    SYMBOL: str = "META"

    database_connection_info: str = create_database_connection_info(
        settings.DB_USER,
        settings.PGPASSWORD,
        settings.DB_HOST,
        settings.DB_PORT,
        settings.DB_NAME
    )
    extract_transform_load(SYMBOL, "OVERVIEW", Company, database_connection_info, PostgresQuery.insert_company)
    extract_transform_load(SYMBOL, "INCOME_STATEMENT", IncomeStatement, database_connection_info, PostgresQuery.insert_income_statement)
    extract_transform_load(SYMBOL, "BALANCE_SHEET",  BalanceSheet, database_connection_info, PostgresQuery.insert_balance_sheet)
    extract_transform_load(SYMBOL, "CASH_FLOW", CashFlow, database_connection_info, PostgresQuery.insert_cash_flow)

if __name__ == "__main__":
    logger.info("Start data pipeline")
    main()
    logger.info("End data pipeline")

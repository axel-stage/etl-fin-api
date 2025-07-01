"""
main module
"""
import argparse
from config import settings
from extract.api_client import fetch_api_data
from transform.schema_alpha_vantage import Company, IncomeStatement, BalanceSheet, CashFlow
from load.database_loader import load_database_engine, insert_into_postgresql
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
    postgres_loader = load_database_engine(insert_into_postgresql)
    postgres_loader(database_connection_info, query, records)

def main():
    """Data Pipeline entrypoint"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--symbol",  type=str, required=True, help= "Define single stock symbol")
    args = parser.parse_args()
    symbol = args.symbol.upper()

    database_connection_info: str = create_database_connection_info(
        settings.DB_USER,
        settings.PGPASSWORD,
        settings.DB_HOST,
        settings.DB_PORT,
        settings.DB_NAME
    )
    extract_transform_load(symbol, "OVERVIEW", Company, database_connection_info, PostgresQuery.insert_company)
    extract_transform_load(symbol, "INCOME_STATEMENT", IncomeStatement, database_connection_info, PostgresQuery.insert_income_statement)
    extract_transform_load(symbol, "BALANCE_SHEET",  BalanceSheet, database_connection_info, PostgresQuery.insert_balance_sheet)
    extract_transform_load(symbol, "CASH_FLOW", CashFlow, database_connection_info, PostgresQuery.insert_cash_flow)

if __name__ == "__main__":
    logger.info("Start data pipeline")
    main()
    logger.info("End data pipeline")

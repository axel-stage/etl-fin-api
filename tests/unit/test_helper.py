import pytest
from datetime import date

from utils.helper import create_api_endpoint, insert_symbol

def test_create_api_endpoint():
    # arrange
    expect = "test.com/query?function=TEST&symbol=ABC&apikey=123Secret"
    # act
    test = create_api_endpoint("test.com/", "TEST", "ABC", "123Secret")
    # assert
    assert test == expect

def test_insert_symbol_value():
    # arrange
    test = [
        {
            "fiscal_date_ending": date(2024, 12, 31),
            "currency": "USD",
            "revenue": 1000000
        },
        {
            "fiscal_date_ending": date(2023, 12, 31),
            "currency": "USD",
            "revenue": 2000000
        }
    ]
    expect = [
        {
            "symbol": "ABC",
            "fiscal_date_ending": date(2024, 12, 31),
            "currency": "USD",
            "revenue": 1000000
        },
        {
            "symbol": "ABC",
            "fiscal_date_ending": date(2023, 12, 31),
            "currency": "USD",
            "revenue": 2000000
        }
    ]
    # act
    insert_symbol("ABC", test)
    # assert
    assert test == expect

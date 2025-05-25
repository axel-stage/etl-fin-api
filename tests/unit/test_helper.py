import pytest
from datetime import date

from utils.helper import create_api_endpoint, insert_symbol, create_database_connection_info

def test_create_api_endpoint():
    # arrange
    expect = "test.com/query?function=TEST&symbol=ABC&apikey=123Secret"
    # act
    test = create_api_endpoint("test.com/", "TEST", "ABC", "123Secret")
    # assert
    assert test == expect

def test_insert_symbol():
    # arrange
    class Test:
        symbol = None
    test = [ Test, Test ]
    class Expect:
        symbol = "ABC"
    expect = [ Expect, Expect]
    # act
    insert_symbol("ABC", test)
    # assert
    assert Test.symbol == Expect.symbol

def test_create_database_connection_info():
    # arrange
    expect = "postgresql://testuser:123Secret@localhost:1234/test_database"
    # act
    test = create_database_connection_info("testuser", "123Secret", "localhost", "1234", "test_database")
    # assert
    assert test == expect

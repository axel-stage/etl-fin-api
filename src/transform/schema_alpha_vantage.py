"""
Pydantic schemas to validate API serialization

Classes:
    ConfigBaseModel
    Company
    IncomeStatementReport
    IncomeStatement
    BalanceSheetReport
    BalanceSheet
    CashFlowReport
    CashFlow
"""

from datetime import date
from pydantic.alias_generators import to_camel, to_pascal
from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
    field_validator
)


class ConfigBaseModel(BaseModel):
    model_config = ConfigDict(
        extra="ignore",
        strict=False,
        str_strip_whitespace=True,
        validate_default=True,
        validate_assignment=True,
        alias_generator=to_camel
    )

    @field_validator("*", mode='before')
    @classmethod
    def none_str_to_none(cls, value: str):
        if value == "None":
            return None
        return value


class Company(ConfigBaseModel):
    model_config = ConfigDict(
        alias_generator=to_pascal
    )

    symbol: str | None = Field(default=None)
    asset_type: str | None = Field(default=None)
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    cik: str | None = Field(default=None, validation_alias="CIK")
    exchange: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    country: str | None = Field(default=None)
    sector: str | None = Field(default=None)
    industry: str | None = Field(default=None)
    address: str | None = Field(default=None)
    official_site: str | None = Field(default=None)
    fiscal_year_end: str | None = Field(default=None)


class IncomeStatementReport(ConfigBaseModel):
    # symbol: str | None = Field(default=None)
    fiscal_date_ending: date
    currency: str = Field(validation_alias="reportedCurrency")
    revenue: int | None = Field(default=None, validation_alias="totalRevenue")
    cost_of_goods_sold: int | None = Field(default=None, validation_alias="costofGoodsAndServicesSold")
    gross_profit: int | None = Field(default=None)
    operating_income: int | None = Field(default=None)
    operating_expenses: int | None = Field(default=None)
    interest_and_debt_expense: int | None = Field(default=None)
    net_income: int | None = Field(default=None)


class IncomeStatement(ConfigBaseModel):
    data: list[IncomeStatementReport] = Field(validation_alias="annualReports")


class BalanceSheetReport(ConfigBaseModel):
    # symbol: str | None = Field(default=None)
    fiscal_date_ending: date
    currency: str = Field(validation_alias="reportedCurrency")
    total_assets: int | None = Field(default=None)
    total_current_assets: int | None = Field(default=None)
    total_non_current_assets: int | None = Field(default=None)
    total_liabilities: int | None = Field(default=None)
    total_current_liabilities: int | None = Field(default=None)
    total_non_current_liabilities: int | None = Field(default=None)
    total_shareholder_equity: int | None = Field(default=None)
    inventory: int | None = Field(default=None)
    current_accounts_payable: int | None = Field(default=None)
    cash_and_cash_equivalents: int | None = Field(default=None, validation_alias="cashAndCashEquivalentsAtCarryingValue")
    current_net_receivables: int | None = Field(default=None)
    shares_outstanding: int | None = Field(default=None, validation_alias="commonStockSharesOutstanding")

    @field_validator(
        "current_net_receivables",
        "inventory",
        mode="after"
    )
    @classmethod
    def none_to_zero(cls, value: int) -> int:
        if value is None:
            return 0
        return value


class BalanceSheet(ConfigBaseModel):
    data: list[BalanceSheetReport] = Field(validation_alias="annualReports")


class CashFlowReport(ConfigBaseModel):
    # symbol: str | None = Field(default=None)
    fiscal_date_ending: date
    currency: str = Field(validation_alias="reportedCurrency")
    cash_flow_operations: int | None = Field(default=None, validation_alias="operatingCashflow")
    cash_flow_investments: int | None = Field(default=None, validation_alias="cashflowFromInvestment")
    cash_flow_financing: int | None = Field(default=None, validation_alias="cashflowFromFinancing")
    dividend_payout: int | None = Field(default=None)

    @field_validator(
        "cash_flow_investments",
        "cash_flow_financing",
        "dividend_payout",
        mode="after"
    )
    @classmethod
    def none_to_zero(cls, value: int) -> int:
        if value is None:
            return 0
        return value


class CashFlow(ConfigBaseModel):
    data: list[CashFlowReport] = Field(validation_alias="annualReports")

CREATE TABLE IF NOT EXISTS staging.income_statement
(
    fiscal_date_ending          DATE          NOT NULL    UNIQUE,
    symbol                      VARCHAR(100)  NOT NULL,
    currency                    CHAR(3)       NOT NULL,
    revenue                     BIGINT,
    cost_of_goods_sold          BIGINT,
    gross_profit                BIGINT,
    operating_income            BIGINT,
    operating_expenses          BIGINT,
    interest_and_debt_expense   BIGINT,
    net_income                  BIGINT
);

CREATE TABLE IF NOT EXISTS staging.cash_flow
(
    fiscal_date_ending    DATE          NOT NULL    UNIQUE,
    symbol                VARCHAR(100)  NOT NULL,
    currency              CHAR(3)       NOT NULL,
    cash_flow_operations  BIGINT,
    cash_flow_investments BIGINT,
    cash_flow_financing   BIGINT,
    dividend_payout       BIGINT
);

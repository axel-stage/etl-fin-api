CREATE TABLE IF NOT EXISTS staging.balance_sheet
(
    fiscal_date_ending              DATE          NOT NULL    UNIQUE,
    symbol                          VARCHAR(100)  NOT NULL,
    currency                        CHAR(3)       NOT NULL,
    total_assets                    BIGINT,
    total_current_assets            BIGINT,
    total_non_current_assets        BIGINT,
    total_liabilities               BIGINT,
    total_current_liabilities       BIGINT,
    total_non_current_liabilities   BIGINT,
    total_shareholder_equity        BIGINT,
    inventory                       BIGINT,
    current_accounts_payable        BIGINT,
    cash_and_cash_equivalents       BIGINT,
    current_net_receivables         BIGINT,
    shares_outstanding              BIGINT
);

CREATE TABLE IF NOT EXISTS staging.company
(
    company_id            SERIAL,
    symbol                VARCHAR(100)  NOT NULL,
    asset_type            VARCHAR(100),
    name                  VARCHAR(1000) NOT NULL,
    description           TEXT,
    cik                   VARCHAR(100),
    exchange              VARCHAR(100),
    currency              CHAR(3),
    country               VARCHAR(100),
    sector                VARCHAR(100),
    industry              VARCHAR(100),
    address               VARCHAR(1000),
    official_site         VARCHAR(1000),
    fiscal_year_end       VARCHAR(100)
);

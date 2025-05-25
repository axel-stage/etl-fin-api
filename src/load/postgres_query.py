class PostgresQuery:
    """Class to store Postgres queries"""
    insert_company = """
    INSERT INTO staging.company (
        symbol,
        asset_type,
        name,
        description,
        cik,
        exchange,
        currency,
        country,
        sector,
        industry,
        address,
        official_site,
        fiscal_year_end
    )
    VALUES (
        %(symbol)s,
        %(asset_type)s,
        %(name)s,
        %(description)s,
        %(cik)s,
        %(exchange)s,
        %(currency)s,
        %(country)s,
        %(sector)s,
        %(industry)s,
        %(address)s,
        %(official_site)s,
        %(fiscal_year_end)s
    );
    """

    insert_income_statement = """
    INSERT INTO staging.income_statement (
        fiscal_date_ending,
        symbol,
        currency,
        revenue,
        cost_of_goods_sold,
        gross_profit,
        operating_income,
        operating_expenses,
        interest_and_debt_expense,
        net_income
    )
    VALUES (
        %(fiscal_date_ending)s,
        %(symbol)s,
        %(currency)s,
        %(revenue)s,
        %(cost_of_goods_sold)s,
        %(gross_profit)s,
        %(operating_income)s,
        %(operating_expenses)s,
        %(interest_and_debt_expense)s,
        %(net_income)s
    );
    """

    insert_balance_sheet = """
    INSERT INTO staging.balance_sheet (
        fiscal_date_ending,
        symbol,
        currency,
        total_assets,
        total_current_assets,
        total_non_current_assets,
        total_liabilities,
        total_current_liabilities,
        total_non_current_liabilities,
        total_shareholder_equity,
        inventory,
        current_accounts_payable,
        cash_and_cash_equivalents,
        current_net_receivables,
        shares_outstanding
    )
    VALUES (
        %(fiscal_date_ending)s,
        %(symbol)s,
        %(currency)s,
        %(total_assets)s,
        %(total_current_assets)s,
        %(total_non_current_assets)s,
        %(total_liabilities)s,
        %(total_current_liabilities)s,
        %(total_non_current_liabilities)s,
        %(total_shareholder_equity)s,
        %(inventory)s,
        %(current_accounts_payable)s,
        %(cash_and_cash_equivalents)s,
        %(current_net_receivables)s,
        %(shares_outstanding)s
    );
    """

    insert_cash_flow = """
    INSERT INTO staging.cash_flow (
        fiscal_date_ending,
        symbol,
        currency,
        cash_flow_operations,
        cash_flow_investments,
        cash_flow_financing,
        dividend_payout
    )
    VALUES (
        %(fiscal_date_ending)s,
        %(symbol)s,
        %(currency)s,
        %(cash_flow_operations)s,
        %(cash_flow_investments)s,
        %(cash_flow_financing)s,
        %(dividend_payout)s
    );
    """

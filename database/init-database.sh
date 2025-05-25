#!/bin/bash
set -e
# connect to postgres db with postgres role
psql -v ON_ERROR_STOP=1 \
    --username ${POSTGRES_USER} \
    --dbname ${POSTGRES_DB} <<EOF
\timing
\conninfo

-- role
CREATE ROLE ${DB_USER}
WITH LOGIN
PASSWORD '$PGPASSWORD'
CONNECTION LIMIT 100
VALID UNTIL 'infinity'
NOCREATEDB
NOSUPERUSER
NOCREATEROLE
NOINHERIT
NOBYPASSRLS
NOREPLICATION;

-- database
CREATE DATABASE ${DB_NAME}
WITH OWNER ${DB_USER}
TEMPLATE template1
ENCODING='UTF8';
\q
EOF

# connect to created db with postgres role
psql -v ON_ERROR_STOP=1 \
    --username ${POSTGRES_USER} \
    --dbname ${DB_NAME} <<EOF
\timing
\conninfo

-- schema
DROP SCHEMA IF EXISTS public CASCADE;
CREATE SCHEMA IF NOT EXISTS ${SCHEMA} AUTHORIZATION ${DB_USER};
SET search_path TO ${SCHEMA};
\q
EOF

# connect to created db with dbuser role
psql -v ON_ERROR_STOP=1 \
  --username=${DB_USER} \
  --dbname=${DB_NAME} <<EOF
\timing
\conninfo
\i schema/ddl_company.sql
\i schema/ddl_income_statement.sql
\i schema/ddl_balance_sheet.sql
\i schema/ddl_cash_flow.sql
\q
EOF

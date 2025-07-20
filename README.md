# ETL Data Pipeline for Finance Data
## Overview
The project goal is to build a data pipeline that extracts, transform and loads real-world finance data on a daily basis from a RESTful API from [Alpha Vantage](https://www.alphavantage.co/) into a relational database.

## Table of Contents
1. [Features](#features)
1. [High Level Architecture](#high-level-architecture)
1. [Technology Stack](#technology-stack)
1. [Prerequisites](#prerequisites)
1. [Installation](#installation)
1. [Usage](#usage)
1. [Clean up](#clean-up)
1. [Lessons Learned](#lessons-learned)
1. [Areas for Improvement](#areas-for-improvement)
1. [License](#license)

## Features
A robust ETL (Extract, Transform, Load) pipeline that ingests real-world finance data from a RESTful API, transforms and validates the data and loads it into a relational database. The system is fully containerized using Docker and supports testing, logging, configuration and secrets management.
 - **ETL**: Automatically fetches financial data from a RESTful API.
 - **Data Validation**: Ensures correctness using pydantic models.
 - **Testing**: Unit tests using pytest.
 - **Configuration Management**: Uses pydantic-settings for environment-based configuration.
 - **Logging**: Structured, persistent logging for audit and debugging.
 - **Argument Parser**: Injects the stock symbol at runtime.
 - **Dockerized**: Reusable Dockerfile with multi-stage build and non-root execution.
 - **Documentation**: Fully documented README.

## High Level Architecture
    ┌───────────────────┐
    │      Extract      │
    │  RESTful API Call │
    └─────────┬─────────┘
              │
    ┌─────────▼─────────┐
    │     Transform &   │
    │     Validate      │
    └─────────┬─────────┘
              │
    ┌─────────▼─────────┐
    │       Load        │
    │                   │
    └───────────────────┘

## Technology Stack
This project leverages modern, containerized tools to build a scalable and maintainable ETL pipeline for financial data.

- **Python** – Powers the extraction and transformation logic.
- **SQL** – Used to load and insert validated data into the database.
- **PostgreSQL** – Serves as the persistent storage layer for the finance dataset.
- **Docker** – Manages local infrastructure, enabling consistent, isolated environments.
- **psql** – PostgreSQL CLI tool for querying and inspecting the database during development.

### Software Components

| Category             | Technology     | Version |
| -------------------- | -------------- | ------- |
| Programming Language | Python         | 3.12.11 |
| Database             | PostgreSQL     | 15.3    |
| Infrastructure       | Docker Desktop | 4.43.1  |
|                      | Docker Engine  | 28.3.0  |
|                      | Docker Compose | 2.38.1  |
| CLI Tool             | psql           | 15.13   |

**Table 1:** Core technology stack used in the project.

## Prerequisites

Before running this project, ensure the following tools are installed on your system:

- Python 3.x
  A modern version of Python (e.g., 3.9 or later) is required to run the pipeline locally or for development purposes.

- Shell Environment
  A Unix-compatible shell such as bash, zsh, or the terminal in your IDE is recommended for executing scripts and commands.

- Docker
  You can use either of the following options based on your preference:

  - [Docker Engine](https://docs.docker.com/engine/install/) (CLI-based):
    Ideal for server environments or users comfortable with command-line tools.

  - [Docker Desktop](https://www.docker.com/products/docker-desktop/) (GUI + CLI):
    Recommended for macOS and Windows users. Provides a user-friendly interface and includes both Docker Engine and Docker Compose.

- Docker Compose
  Included by default in Docker Desktop. If you’re using Docker Engine on Linux, you may need to [install Docker Compose separately](https://docs.docker.com/compose/install/).

- `psql` – PostgreSQL Command Line Interface
  Useful for manually inspecting or querying the database during development and debugging.

  Installation:

  - **macOS**: `brew install postgresql`
  - **Ubuntu/Debian**: `sudo apt install postgresql-client`
  - **Windows**: Included with [PostgreSQL installer](https://www.postgresql.org/download/windows/)

## Installation
To install the pipeline on a Linux distribution or WSL follow these steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/axel-stage/etl-fin-api
    ```
1. Navigate to the project directory:
    ```bash
    cd etl-fin-api
    ```
1. Create a env file for environment variables:
    ```bash
    cat <<EOF > .env
    ENVIRONMENT=dev
    BASE_URL=https://www.alphavantage.co/
    POSTGRES_IMAGE=postgres:15.3
    POSTGRES_PORT=5432:5432
    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    DB_HOST=database
    DB_PORT=5432
    DB_NAME=finance_db
    DB_USER=dbadmin
    SCHEMA=staging
    PGPASSWORD=<DATABASE PASSWORD PLACEHOLDER>
    API_KEY=<API KEY PLACEHOLDER>
    EOF
    ```
1. Claim your Free API Key: https://www.alphavantage.co/support/#api-key
1. Replace "\<API KEY PLACEHOLDER>" with your API Key in .env file
1. Replace "\<DATABASE PASSWORD PLACEHOLDER>" with your password in .env file

## Usage
1. Build & run the Compose stack in detached mode:
    ```bash
    docker compose up -d --build
    ```
1. After the database is initialized, the ETL process is started automatically request finance data from MSFT stock.
1. Run further ETL jobs:
    ```bash
    docker compose run --rm etl-fin-api --symbol AAPL
    ```
1. Verify inserted data with psql tool:
    ```bash
    source .env
    export PGPASSWORD=$PGPASSWORD
    psql -h localhost -p ${DB_PORT} -d ${DB_NAME} -U ${DB_USER} <<EOF
    \pset linestyle unicode
    \pset unicode_border_linestyle single
    \pset unicode_column_linestyle single
    \pset unicode_header_linestyle double
    \pset format wrapped
    \pset columns 0
    \! clear
    SELECT * FROM staging.company;
    EOF
    ```
    You should see two rows in the database containing the compony infos from Microsoft and Apple.

## Clean up
Remove container, networks, **volumes** and images defined in the Compose file:<br>
**Persistent data will be deleted!**
```bash
docker compose down --volumes --rmi local
```

## Lessons Learned
- Pydantic has proven to be a reliable and efficient tool for data validation, especially when working with serialized/deserialized data.
- The `pydantic-settings` package significantly simplifies configuration management, particularly for handling secrets securely and cleanly.
- The current Dockerfile design is solid and will serve as a strong reference for future Python-based container builds im my projects.
- Implementing health checks for the database container was crucial in resolving timing issues between service startups, ensuring the pipeline only starts when dependencies are ready.

## Areas for Improvement
- Optimize Docker Image Size: Further reduce the Docker image footprint by leveraging slimmer base images.
- Enhance Test Coverage: Add more unit and integration tests to increase pipeline robustness.

## License
This project is licensed under the MIT license.
See [LICENSE](LICENSE) for more information.

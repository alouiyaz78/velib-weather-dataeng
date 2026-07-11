<div align="center">
    <img src="https://github.com/user-attachments/assets/4f74dcb8-b636-48c9-b1fd-8dcd3b8c84fb" alt="Logo" height="120" width="210">
</div>

<div align="center">
    <h1>Projet Data Engineering - Influence de la météo sur le parc de Vélib à Paris</h1>
</div>

Ce projet a pour objectif de collecter et analyser les données des **Velib** et de la **météo** à Paris. Nous allons utiliser les API de [Open Data Paris](https://opendata.paris.fr/pages/home/) et de [Open Meteo](https://open-meteo.com/en/docs) pour récupérer les données en temps réel, puis les stocker dans une base PostgreSQL.

<div align="center">
    <img width="3739" height="1178" alt="Pipeline tools" src="https://github.com/user-attachments/assets/54f94962-17da-4428-970f-69c1fe7f4277" />
</div>

## Tech Stack

- Ingestion: Python, httpx, psycopg2, pydantic-settings
- Orchestration: Apache Airflow (LocalExecutor)
- Storage: PostgreSQL, medallion architecture (bronze / silver / gold)
- Transformation and Testing: dbt (dbt-postgres)
- API layer: FastAPI
- Dashboard: Streamlit, Plotly
- Containerization: Docker, Docker Compose
- Alerting: SMTP email notifications on pipeline failure

## Project Structure

- ingestion/ : Python fetchers for Velib and weather APIs
- DBT/ : dbt project (staging, intermediate, marts models)
- airflow/ : Airflow DAGs orchestrating ingestion and dbt
- dashboard/ : FastAPI backend and Streamlit frontend
- postgres/ : Database initialization scripts
- API Docs/ : Source API documentation
- docker-compose.yml : Full stack orchestration

## Data Pipeline

Bronze: raw data as received from the APIs, deduplicated on natural keys (station code plus timestamp), refreshed every 10 minutes via Airflow.

Silver: cleaned and renamed columns, boolean conversions, timezone-aware timestamps.

Gold: fct_velib_meteo, a single ML-ready fact table joining each Velib station snapshot with its nearest weather reading (plus or minus 15 min window via a LATERAL JOIN), enriched with time-based features (hour, day of week, month, weekend flag) and the target variable, occupancy_rate.

Data quality is enforced with 18 dbt tests (not_null, unique, accepted_values) across sources and models.

## Orchestration

A single Airflow DAG (velib_pipeline) runs every 10 minutes:

fetch_velib and fetch_meteo run in parallel, then dbt_run, then dbt_test.

Email alerts are sent automatically if any task fails after retry.

## Getting Started

### Prerequisites

Docker and Docker Compose, plus a .env file (see .env.example for required variables).

### Run the full stack

docker compose up -d

This starts PostgreSQL, the ingestion service, Airflow (webserver and scheduler), and the dashboard.

### Access points

Dashboard (Streamlit): http://localhost:8501

Dashboard API (FastAPI): http://localhost:8000

Airflow UI: http://localhost:8081

### Run dbt manually (optional, Airflow handles this automatically)

docker compose run --rm dbt uv run dbt run

docker compose run --rm dbt uv run dbt test

### Generate dbt documentation

docker compose run --rm -p 8080:8080 dbt sh -c "uv run dbt docs generate && uv run dbt docs serve --port 8080 --host 0.0.0.0"

## Data Sources

Velib real-time availability: https://opendata.paris.fr/ (Paris Open Data, GBFS standard)

Open-Meteo: https://open-meteo.com/ (free weather API, no key required)

## Author

Yazid Aloui

github.com/alouiyaz78

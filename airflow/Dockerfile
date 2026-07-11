FROM apache/airflow:2.10.3-python3.12

USER root

# Certificats pour les téléchargements HTTPS
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

USER airflow

# Dépendances Python : ingestion (fetchers) + dbt
RUN pip install --no-cache-dir \
    httpx \
    psycopg2-binary \
    pydantic-settings \
    dbt-postgres==1.9.0
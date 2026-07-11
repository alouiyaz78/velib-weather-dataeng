import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

sys.path.insert(0, "/opt/airflow/ingestion")

from fetchers.velib_fetcher import VelibFetcher
from fetchers.meteo_fetcher import MeteoFetcher


def run_velib_fetcher():
    VelibFetcher().run()


def run_meteo_fetcher():
    MeteoFetcher().run()


default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="velib_pipeline",
    description="Collecte Vélib + météo, transformations dbt, orchestrées par Airflow",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule=timedelta(minutes=10),
    catchup=False,
    tags=["velib"],
) as dag:

    fetch_velib = PythonOperator(
        task_id="fetch_velib",
        python_callable=run_velib_fetcher,
    )

    fetch_meteo = PythonOperator(
        task_id="fetch_meteo",
        python_callable=run_meteo_fetcher,
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/dbt_project && dbt run",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/airflow/dbt_project && dbt test",
    )

    [fetch_velib, fetch_meteo] >> dbt_run >> dbt_test

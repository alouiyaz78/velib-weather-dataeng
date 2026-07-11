from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def hello():
    print("Le DAG de test fonctionne !")

with DAG(
    dag_id="test_dag",
    description="DAG minimal pour vérifier que l'infrastructure fonctionne",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["test"],
) as dag:
    task_hello = PythonOperator(
        task_id="hello_task",
        python_callable=hello,
    )

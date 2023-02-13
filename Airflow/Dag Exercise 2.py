from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import json
from datetime import datetime, timedelta

def python_first_function():
    date = datetime.now()
    date = date.strftime("%Y-%m-%d %H:%M:%S")
    json_data = json.dumps(date)
    return json_data

default_dag = {
    'start_date': datetime(2022,12,1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'project_id': 1
}

with DAG("exercise_2", schedule_interval='@daily', catchup=False, default_args=default_dag) as dag_python:
    task0=PythonOperator(task_id="second_task", python_callable=python_first_function)
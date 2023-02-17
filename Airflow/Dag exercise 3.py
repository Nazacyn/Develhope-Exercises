import requests
import time
import json
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

# exercise: write a DAG which is able to request market data for a list of stocks.
api_key = '2WRZMAU9MOTPZK0X'

def get_data():

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey='+api_key
    r = requests.get(url)
    try:
        data = r.json()
        path ="C:/Users/S3 Audio Visual/testtData_center/Data_lake"
        with open(path + "stock_market_raw_data" + "IBM" + str(time.time()), "w") as outfile:
            json.dump(data, outfile)
    except:
        pass


default_dag_args = {
    'start_date': datetime(2023, 2, 16),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
    'project_id': 1 }


with DAG("market_data_alphavantage_dag", schedule_interval = '@daily', catchup=False, default_args = default_dag_args) as dag_python:
    # here we define our tasks
    task_0=PythonOperator(task_id = "get_market_data", python_callable=get_data)
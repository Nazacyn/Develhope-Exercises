from airflow import DAG 
from airflow.operators.bash_operator import BashOperator 
from datetime import datetime, timedelta

default_dag_args = { 
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=2),
    'project_id': 1
}

with DAG("First_DAG", schedule_interval=None, default_args=default_dag_args) as dag:

    task_0 = BashOperator(task_id='bash_task', bash_command="echo 'command executed from Bash Operator' ")
    task_1 = BashOperator(task_id='bash_task_move_data', bash_command="cp /Users/S3 Audio Visual/testt/Data_center/Data_lake/dataset_raw.txt /Users/S3 Audio Visual/testt/Data_center/Clean_data")
    task_2 = BashOperator(task_id='bash_task_remove_file', bash_command="rm /Users/S3 Audio Visual/testt/Data_center/Data_lake/dataset_raw.txt")


    task_0 >> task_1 >> task_2

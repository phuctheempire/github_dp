from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'xpham',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_schedule_cron_v3', 
    default_args=default_args,
    start_date=datetime(2025, 8,1),
    end_date=datetime(2025, 9, 23),
    schedule='0 */12 * 8,9 2,4', 
    catchup=True
) as dag:
    task1 = BashOperator(
        task_id='task_1_bash',
        bash_command='echo "This DAG runs at 6 AM every weekday. From 1 to 21 Sep, Catchup normally skip 6, 7, 13,14, 20, 21 Sep"',
    )
    task1

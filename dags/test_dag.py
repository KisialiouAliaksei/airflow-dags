from datetime import datetime, timedelta

from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 6, 2),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

example_workflow = DAG('kube-operator',
                         default_args=default_args,
                         schedule_interval=timedelta(days=1))

with example_workflow:
    t1 = KubernetesPodOperator(namespace='airflow',
                               image="python:3.6",
                               cmds=["python","-c"],
                               arguments=["print('hello world')"],
                               labels={'runner': 'airflow'},
                               name="pod1",
                               task_id='pod1',
                               is_delete_operator_pod=True,
			       get_logs=True,
                               hostnetwork=False,
                               )

    t1
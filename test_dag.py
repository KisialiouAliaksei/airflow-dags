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
    "retries": 0 
}

dag = DAG('kube-operator',default_args=default_args,schedule_interval=timedelta(days=1))

task = KubernetesPodOperator(namespace='air-eks-exp',
                               image="python:3.6-slim",
                               cmds=["python","-c"],
                               arguments=["print('hello world')"],
                               labels={"app": "test-creatives-task"},
			       startup_timeout_seconds=30,
                               name="pod1",
                               task_id='pod1',
			       hostnetwork=False,
                               is_delete_operator_pod=False,
			       get_logs=True,
			       in_cluster=True,
			       do_xcom_push=False,
			       dag=dag)

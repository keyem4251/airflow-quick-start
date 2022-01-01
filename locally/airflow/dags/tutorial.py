from datetime import datetime, timedelta
from logging import FATAL
from textwrap import dedent

from airflow import DAG

from airflow.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["ariflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    "tutorial",
    default_args=default_args,
    description="A simple tutoril DAG.",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022, 1, 1),
    catchup=False,
    tags=["example"]
) as dag:

    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    t2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
    )

    t1.doc_md = dedent(
        """\
            #### Task Documentation
            You can document your task using the attributes `doc_md`(markdown),
            `doc`(plain text), `dock_rst`, `doc_json`, `doc_yaml` which gets rendered in the UI's Task Instance Details page.
            ![img](......)
        """
    )

    dag.doc_md = __doc__
    dag.doc_md = """
    This is a documentation placed anywhere
    """

    templated_command = dedent(
        """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7) }}"
        echo "{{ params.my_param }}"
    {% endfor %}
        """
    )

    t3 = BashOperator(
        task_id="templated",
        depends_on_past=False,
        bash_command=templated_command,
        params={"myparam": "Parameter I passed in"}
    )

    t1 >> [t2, t3]

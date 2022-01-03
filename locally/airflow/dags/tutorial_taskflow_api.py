import json
from datetime import datetime

from airflow.decorators import dag, task

@dag(
    task_id="tutorial_etl_dag_example",
    scheduler_interval=None,
    start_date=datetime(2022, 1, 1),
    catachup=False,
    tags=["example"]
)
def tutorial_taskflow_api_etl():
    
    @task()
    def extract():
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
        order_data_dict = json.loads(data_string)
        return order_data_dict

    @task(multiple_outputs=True)
    def transaform(order_data_dict: dict):
        total_order_value = 0
        
        for value in order_data_dict.values():
            total_order_value += value

        return {"total_order_value": total_order_value}

    @task()
    def load(total_order_value: float):
        print(f"Total order value is: {total_order_value:.2f}")

    order_data = extract()
    order_summary = transaform(order_data)
    load(order_summary["total_order_value"])

tutorial_etl_dag = tutorial_taskflow_api_etl()

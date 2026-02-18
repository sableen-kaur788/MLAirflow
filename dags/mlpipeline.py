from airflow.sdk import task, dag
from datetime import datetime

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append("C:\\Users\\sable\\MLAirflow")

from src.cleaning import clean_data
from src.preprocessing import preprocess_data


@dag(dag_id="ml_pipline")
def ml_pipline():

    @task(task_id="cleaning")
    def cleaning():
        clean_data()

    @task(task_id="pre_processing")
    def pre_processing():
        preprocess_data()

    cleaning() >> pre_processing()


ml_pipline()

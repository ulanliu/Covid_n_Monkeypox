import requests
from datetime import date
from pathlib import Path
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials
import os
import logging
from gcs_to_bq_flow import load_data_from_gcs_to_bq
from prefect_dbt_flow import trigger_dbt_cli_command_flow

@task(retries=3, log_prints=True)
def extract(url: str) -> Path:
    """
    Download monkeypox and covid-19 daily data from Our World In Data into local
    """
    day = date.today().strftime('%Y%m%d')
    if 'monkeypox' in url:
        path = Path(f'data/monkeypox_{day}.csv')
        r = requests.get(url)
        if not os.path.isdir('data'):
            os.mkdir('data')
        with open(path, 'w+') as f:
            f.write(r.text)
        logging.info("successfully download latest monkeypox data")
    
    if 'covid' in url:
        path = Path(f'data/covid19_{day}.csv')
        r = requests.get(url)
        if not os.path.isdir('data'):
            os.mkdir('data')
        with open(path, 'w+') as f:
            f.write(r.text)
        logging.info("successfully download latest covid-19 data")

    return path

@task(retries=3 ,log_prints=True)
def load_data_to_gcs(path: Path) -> str:
    """
    Load the data into GCS and return the GCS path
    """
    gcs_block = GcsBucket.load("zoomcamp")
    gcs_block.upload_from_path(from_path=path, to_path=path)

    if 'monkeypox' in str(path):
        table_name = 'monkeypox'
    if 'covid' in str(path):
        table_name = 'covid19'
    day = date.today().strftime('%Y%m%d')
    gcs_path = f'gs://dtc_who_data_lake_de-zoomcamp-378315/data/{table_name}_{day}.csv'

    return gcs_path

@flow()
def who_data_elt_flow(url: str) -> None:
    path = extract(url)
    gcs_path = load_data_to_gcs(path)
    bq_task = load_data_from_gcs_to_bq(gcs_path)
    

@flow()
def elt_parent_flow(
        url_list: list[str]=["https://raw.githubusercontent.com/owid/monkeypox/main/owid-monkeypox-data.csv", "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"],
        dbt_command: str="dbt run"
    ) -> None:
    """ The main flow function """
    for url in url_list:
        who_data_elt_flow(url)
    trigger_dbt_cli_command_flow(dbt_command)

if __name__ == "__main__":
    elt_parent_flow()

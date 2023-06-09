from prefect import flow, task
from prefect_gcp import GcpCredentials
from prefect_gcp.bigquery import bigquery_load_cloud_storage
from pathlib import Path

@flow()
def load_data_from_gcs_to_bq(gcs_path: str):
    """
    Transfer data from GCS to BQ
    """
    gcp_credentials_block = GcpCredentials.load("zoomcamp") # Use the block name you created
    
    if 'monkeypox' in gcs_path:
        table_name = 'monkeypox' # change the name if you want
    if 'covid' in gcs_path:
        table_name = 'covid19' # change the name if you want
    
    result = bigquery_load_cloud_storage(
        dataset='who_disease_data', # change the name if you want
        table=table_name,
        uri=gcs_path,
        gcp_credentials=gcp_credentials_block
    )

    return result
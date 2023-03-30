from typing import Optional
import argparse
from prefect.blocks.core import Block
from pydantic import SecretStr
from pathlib import Path
from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket

def main(params):
    """
    Create prefect blocks
    """
    service_account_file = params.service_account_file
    gcp_credentials_block_name = params.gcp_credentials_block_name
    gcs_bucket_name = params.gcs_bucket_name
    gcs_bucket_block_name = params.gcs_bucket_block_name
    
    gcp_credentials_block = GcpCredentials(service_account_file=service_account_file)
    gcp_credentials_block.save(gcp_credentials_block_name, overwrite=True)

    gcp_credentials = GcpCredentials.load(gcp_credentials_block_name)
    gcs_bucket_block = GcsBucket(bucket=gcs_bucket_name, gcp_credentials=gcp_credentials)
    gcs_bucket_block.save(gcs_bucket_block_name, overwrite=True)

    print('successfully created blocks')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create GcpCredentials Block and GcsBucket Block')
    
    parser.add_argument('--service_account_file', help='path for gcp_credentials_file')
    parser.add_argument('--gcp_credentials_block_name', help='name for gcp_credentials_block')
    parser.add_argument('--gcs_bucket_name', help='name for bucket_name')
    parser.add_argument('--gcs_bucket_block_name', help='name for gcs_bucket_block_name')

    args = parser.parse_args()
    main(args)


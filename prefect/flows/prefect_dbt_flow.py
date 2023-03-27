from prefect import flow
from prefect_dbt.cli.commands import trigger_dbt_cli_command

@flow(retries=3)
def trigger_dbt_cli_command_flow(command:str):
    result = trigger_dbt_cli_command(
        command=command,
        project_dir='${HOME}/DE_zoomcamp_project/dbt/who_disease_data'
    )
    return result


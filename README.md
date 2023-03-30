# DE zoomcamp Project - Covid-19 and Monkeypox number by Country

## Overview

This project was executed as a part of the Data Engineering Zoomcamp course held by DataTalks.Club. The goal of this project is to apply everything we learned in this course and build an end-to-end data pipeline.

## Problem description

This project is related to covid-19 and monkeypox diseases. Which area has highest prevalence rate? Does the high covid-19 prevalence rate also have high monkeypox prevalence rate? How is the case fatality rate between covid-19 and monkeypox.

## Dataset

The data resource is form [Our World in Data](https://github.com/owid)

### who_disease
```
	|- **location** string
	|- **iso_code** string
	|- **date** string
	|- **monkeypox_total_cases** float
	|- **monkeypox_total_deaths** float
	|- **monkeypox_new_cases** float
	|- **monkeypox_new_deaths** float
	|- **monkeypox_new_cases_smoothed** float
	|- **monkeypox_new_deaths_smoothed** float
	|- **monkeypox_new_cases_per_million** float
	|- **monkeypox_total_cases_per_million** float
	|- **monkeypox_new_cases_smoothed_per_million** float
	|- **monkeypox_new_deaths_per_million** float
    |- **monkeypox_total_deaths_per_million** float
	|- **monkeypox_new_deaths_smoothed_per_million** float
    |- **covid19_total_cases** float
	|- **covid19_total_deaths** float
    |- **covid19_new_cases** float
	|- **covid19_new_deaths** float
    |- **covid19_new_cases_smoothed** float
	|- **covid19_new_deaths_smoothed** float
    |- **covid19_new_cases_per_million** float
	|- **covid19_total_cases_per_million** float
    |- **covid19_new_cases_smoothed_per_million** float
	|- **covid19_new_deaths_per_million** float
    |- **covid19_total_deaths_per_million** float
	|- **covid19_new_deaths_smoothed_per_million** float
```

## Technologies

- Google cloud Platform
  - Compute Engine (Optional)
  - Cloud Storage
  - Bigquery
- Terraform
- prefect
- dbt
- Looker

## Project architecture

![Project architecture](image/de-zoomcamp_project_flow_chart.png)  

## Prequisites

- Python 3 (installed with Anaconda)
- Google Cloud SDK
- Terraform

## GCP setup

Please follow this [note](https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes/1_intro.md#user-content-gcp-initial-setup).
  
If you have problems setting up the env, you can create a virtual machine for this project.  
Please follow this video and only need to follow these part:  
- Generating SSH keys
- Creating a virtual machine on GCP
- Connecting to the VM with SSH
- Installing Anaconda
- Creating SSH config file
- Accessing the remote machine with VS Code and SSH remote
- Installing Terraform
  
## Reproduction steps

1. Fork this repo

2. Clone your folked repo
```
git clone <your-repo-url>
cd DE_ZOOMCAMP_PROJECT
```

3. 
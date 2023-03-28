{{ config(materialized='table') }}

{%- set cols = adapter.get_columns_in_relation(source('staging', 'monkeypox')) -%}

WITH monkeypox AS (
    SELECT
        {% for col in cols %}
            monkeypox.{{col.name}} AS monkeypox_{{col.name}},
        {% endfor %}
    FROM {{ source('staging', 'monkeypox') }}
),

covid19 AS (
    SELECT 
        {% for col in cols %}
            covid19.{{col.name}} AS covid19_{{col.name}},
        {% endfor %}
    FROM {{ source('staging', 'covid19') }}
)

SELECT 
    covid19_location AS location,
    covid19_iso_code AS iso_code,
    covid19_date AS date,
    monkeypox_total_cases,
    monkeypox_total_deaths,
    monkeypox_new_cases,
    monkeypox_new_deaths,
    monkeypox_new_cases_smoothed,
    monkeypox_new_deaths_smoothed,
    monkeypox_new_cases_per_million,
    monkeypox_total_cases_per_million,
    monkeypox_new_cases_smoothed_per_million,
    monkeypox_new_deaths_per_million,
    monkeypox_total_deaths_per_million,
    monkeypox_new_deaths_smoothed_per_million,
    covid19_total_cases,
    covid19_total_deaths,
    covid19_new_cases,
    covid19_new_deaths,
    covid19_new_cases_smoothed,
    covid19_new_deaths_smoothed,
    covid19_new_cases_per_million,
    covid19_total_cases_per_million,
    covid19_new_cases_smoothed_per_million,
    covid19_new_deaths_per_million,
    covid19_total_deaths_per_million,
    covid19_new_deaths_smoothed_per_million
FROM covid19 AS c
LEFT JOIN monkeypox AS m
    ON c.covid19_iso_code = m.monkeypox_iso_code AND c.covid19_date = m.monkeypox_date
WHERE covid19_location != "World"

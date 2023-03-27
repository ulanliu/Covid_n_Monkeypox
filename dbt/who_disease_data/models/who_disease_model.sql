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
        -- location,
        -- iso_code,
        -- date,
        -- total_cases,
        -- total_deaths,
        -- new_cases,
        -- new_deaths,
        -- new_cases_smoothed,
        -- new_deaths_smoothed,
        -- new_cases_per_million,
        -- total_cases_per_million,
        -- new_cases_smoothed_per_million,
        -- new_deaths_per_million,
        -- total_deaths_per_million,
        -- new_deaths_smoothed_per_million
    FROM {{ source('staging', 'covid19') }}
)

SELECT * 
FROM covid19 AS c
LEFT JOIN monkeypox AS m
    ON c.covid19_iso_code = m.monkeypox_iso_code AND c.covid19_date = m.monkeypox_date


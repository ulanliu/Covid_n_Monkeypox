{{ config(materialized='table') }}

{%- set cols = adapter.get_columns_in_relation(source('staging', 'monkeypox')) -%}

WITH monkeypox AS (
    SELECT
        *,
        'monkeypox' AS disease_type
    FROM {{ source('staging', 'monkeypox') }}
),

covid19 AS (
    SELECT 
        {% for col in cols %}
            covid19.{{col.name}} AS {{col.name}},
        {% endfor %}
        'covid19' AS disease_type
    FROM {{ source('staging', 'covid19') }}
),

diseases_unioned AS (
    SELECT * FROM monkeypox
    UNION ALL
    SELECT * FROM covid19
)

SELECT 
    *
FROM diseases_unioned
WHERE location != "World"
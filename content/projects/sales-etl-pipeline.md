---
title: "Sales ETL Pipeline"
summary: "Batch ETL that takes a messy sales export, cleans and tests it, and loads it into a SQLite warehouse that refuses bad data."
date: 2026-09-22
tags: ["python", "sql", "data-engineering", "pandas"]
---

The input is generated to look like a real CRM export: mixed date and currency formats, duplicate rows, and orders pointing at customers who no longer exist. The pipeline cleans it, and six data-quality checks gate every run (null keys, duplicate orders, both foreign keys, negative totals, quarantine rate). If any check fails the run exits non-zero and CI goes red.

The tests caught a real bug on the way: `to_sql(if_exists="replace")` was quietly dropping the schema's primary and foreign keys. It now loads into the existing constrained schema instead.

**Stack:** Python, pandas, SQLite, pytest, GitHub Actions

**Repo:** [sales-etl-pipeline](https://github.com/eddyndumia/sales-etl-pipeline)

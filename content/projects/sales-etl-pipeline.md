---
title: "Sales ETL Pipeline"
summary: "End-to-end batch ETL: a deliberately messy raw sales export cleaned, tested, and loaded into a quality-gated SQLite warehouse."
date: 2026-09-22
tags: ["python", "sql", "data-engineering", "pandas"]
---

A data engineering portfolio piece built to prove the pipeline can be trusted, not just eyeballed. The raw input is synthetically generated to reproduce exactly the mess a real CRM/billing export produces — mixed date formats, mixed currency formatting, duplicate rows, orders referencing a customer who no longer exists — and the pipeline's job is to clean it with tests and automated checks backing every claim.

Six automated data-quality checks gate every run (null primary keys, duplicate order IDs, referential integrity on both foreign keys, no negative order totals, a bounded quarantine rate) and the pipeline exits non-zero — failing CI — if any of them fail. A real bug the test suite caught during development: `DataFrame.to_sql(if_exists="replace")` was silently dropping the hand-written schema's `PRIMARY KEY`/`REFERENCES` constraints; fixed by loading into the existing constrained schema instead.

**Tech stack:** Python, pandas, SQLite, pytest, GitHub Actions

**Repo:** [sales-etl-pipeline](https://github.com/eddyndumia/sales-etl-pipeline)

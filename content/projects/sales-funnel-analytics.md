---
title: "Sales Pipeline Funnel Analytics"
summary: "SQL-driven B2B sales pipeline analysis: funnel drop-off, rep and lead-source win rates, deal velocity by segment, stage-weighted revenue forecasting."
date: 2026-09-22
tags: ["sql", "python", "data-analysis"]
---

Six standalone SQL queries answering the questions a sales-ops team actually asks: where in the funnel deals are lost (biggest single drop is Qualified → Proposal, at 55.6%), which reps and lead sources really convert (a 4x win-rate spread between the top and bottom rep on the same lead pool), how deal velocity scales with deal size (Enterprise deals take ~2.8x longer to close than SMB), and what the open pipeline is realistically worth once weighted by stage.

Tested against a small hand-built fixture database with known-correct answers, deliberately not against the generated sample data — that way the tests keep proving the SQL itself is correct even if the data generator's parameters change later.

**Tech stack:** SQL (SQLite), Python, pandas, matplotlib

**Repo:** [sales-funnel-analytics](https://github.com/eddyndumia/sales-funnel-analytics)

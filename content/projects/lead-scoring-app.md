---
title: "Lead Scoring App"
summary: "A lead-scoring classifier deployed as a real Streamlit app, with precision/recall thresholds tied to actual sales team capacity instead of a bare accuracy score."
date: 2026-09-22
tags: ["python", "machine-learning", "streamlit", "scikit-learn"]
---

A gradient-boosting lead-scoring model (0.70 ROC-AUC) wrapped in a Streamlit app with three tabs: score a single lead by hand, upload a CSV to rank a whole batch, or check a capacity guide showing exactly what precision/recall a sales team should expect at its real weekly contact capacity — at 25% capacity, contacting the model's top-scored quarter of leads catches 48% of actual converters at 35.7% precision, roughly a 1.9x lift over contacting a random 25%.

Also fixes a real, easy-to-miss bug: one-hot encoding a single new lead only produces dummy columns for the categories present in that one row, which would otherwise crash or silently misalign against a model trained on the full category set. `align_columns` reindexes any new data against the model's exact training columns — covered directly by tests, not just fixed and left unverified.

**Tech stack:** Python, scikit-learn, Streamlit, pandas

**Repo:** [lead-scoring-app](https://github.com/eddyndumia/lead-scoring-app)

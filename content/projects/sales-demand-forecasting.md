---
title: "Sales Demand Forecasting"
summary: "Daily sales forecast 90 days out, comparing seasonal-naive, SARIMA and XGBoost, and why SARIMA misses the holiday spike."
date: 2026-09-22
tags: ["python", "time-series", "statsmodels", "xgboost"]
---

XGBoost came out best (5.76% MAPE), then the seasonal-naive baseline (6.69%), and SARIMA was far behind (19.85%). The interesting part is why. SARIMA's error was 6.5x higher in November and December, because its seasonal period is weekly and it has no way to see the yearly holiday spike. XGBoost gets it from a plain calendar feature. A classical model only knows the seasonality you give it.

The train/test split is by date, not random, because shuffling a time series inflates every score until the model meets the real future.

**Stack:** Python, statsmodels, XGBoost, scikit-learn, matplotlib

**Repo:** [sales-demand-forecasting](https://github.com/eddyndumia/sales-demand-forecasting)

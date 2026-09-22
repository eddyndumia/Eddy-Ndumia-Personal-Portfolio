---
title: "Sales Demand Forecasting"
summary: "Seasonal-naive vs. SARIMA vs. XGBoost on a 90-day holdout — with a real finding on why single-seasonality classical models miss yearly retail spikes."
date: 2026-09-22
tags: ["python", "time-series", "statsmodels", "xgboost"]
---

Forecasts daily sales revenue 90 days out and explains a genuine, counterintuitive result rather than just reporting numbers: the classical SARIMA model does dramatically worse (19.85% MAPE) than both a seasonal-naive baseline (6.69%) and a feature-engineered XGBoost model (5.76%, the best of the three). Digging into *why* — SARIMA's error is 6.5x higher in November/December than October, because its weekly-only seasonal period has no way to anticipate the built-in yearly Nov/Dec demand spike, while XGBoost captures it via an explicit calendar feature. A classical model is only as good as the seasonal structure you explicitly give it.

The train/test split is chronological, not random, with the reasoning for that documented directly in the code — shuffling a time series before splitting silently inflates every accuracy number in a way that looks fine until the model meets real future data.

**Tech stack:** Python, statsmodels, XGBoost, scikit-learn, matplotlib

**Repo:** [sales-demand-forecasting](https://github.com/eddyndumia/sales-demand-forecasting)

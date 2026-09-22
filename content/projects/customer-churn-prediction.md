---
title: "Customer Churn Classification"
summary: "Churn prediction with a real business-dollar payoff, not just an accuracy score — EDA, imbalance-aware model comparison, confusion matrix translated into $ saved."
date: 2026-09-22
tags: ["python", "machine-learning", "scikit-learn", "xgboost"]
---

Most churn portfolio projects stop at an accuracy number. This one compares five model/imbalance-handling combinations (logistic regression and random forest each with class weighting vs. SMOTE, plus XGBoost with `scale_pos_weight`) on a realistically imbalanced 24.8% churn rate, then translates the winning model's confusion matrix into an actual dollar figure: on the held-out test set, flagging high-risk customers for retention outreach nets an estimated $112k benefit over contacting nobody, against explicit, stated assumptions about outreach cost and retained-customer value.

The winner by ROC-AUC was class-weighted logistic regression — not the more complex tree ensembles — a genuine finding from the comparison, not a foregone conclusion picked in advance.

**Tech stack:** Python, scikit-learn, imbalanced-learn, XGBoost, matplotlib

**Repo:** [customer-churn-prediction](https://github.com/eddyndumia/customer-churn-prediction)

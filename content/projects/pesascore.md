---
title: "PesaScore"
summary: "Alt-data credit scoring platform that scores creditworthiness from M-Pesa statements instead of a traditional credit bureau."
date: 2026-09-13
tags: ["fintech", "python", "typescript", "postgres"]
---

A fintech platform built from the ground up to score creditworthiness from alternative data — starting with M-Pesa statements — instead of relying on a traditional credit bureau. Two front-facing apps (a consumer app and a lender dashboard) run on real multi-tenant identity and consent flows, backed by a Postgres/Supabase data layer. Originally shipped as *ScoreWise*, renamed to PesaScore as the product sharpened.

**Tech stack:** TypeScript, Python, Postgres/Supabase

**Repos:**
- [scorewise](https://github.com/eddyndumia/scorewise) — consumer + lender frontend
- [score-wise-backend](https://github.com/eddyndumia/score-wise-backend) — API and scoring backend

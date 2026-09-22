---
title: "PesaScore"
summary: "Alt-data credit scoring platform that scores creditworthiness from M-Pesa statements instead of a traditional credit bureau."
date: 2026-09-13
tags: ["fintech", "python", "typescript", "postgres"]
---

PesaScore scores creditworthiness from a person's actual M-Pesa transaction history instead of a credit bureau file most people in Kenya don't have. A borrower uploads their M-Pesa statement PDF in the consumer app, the backend parses it and runs the real scoring logic against it — not a mock, an actual number comes out the other end. On the other side, a lender (a SACCO or microlender) logs into a separate dashboard to review applicants: score breakdown, applicant list, approval stats.

Two apps, one backend. Auth runs on Supabase, with Postgres Row Level Security keeping one lender's applicant data walled off from another's — actual tenant isolation, not just an app-level filter. Started under the name *ScoreWise*; renamed to PesaScore once the product direction (alt-data scoring specifically, not a general fintech app) was locked in.

**Tech stack:** TypeScript (React), Python (FastAPI), Postgres/Supabase

**Repos:**
- [scorewise](https://github.com/eddyndumia/scorewise) — consumer (borrower) app
- [score-wise-backend](https://github.com/eddyndumia/score-wise-backend) — statement parsing, scoring, and the lender API

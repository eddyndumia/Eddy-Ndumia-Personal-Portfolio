---
title: "GBL Capital"
summary: "Customer app, desk app and backend for a futures signals service. Ten releases in two days, up to 2.0.0. Backend built and tested, not yet deployed."
date: 2026-10-10
tags: ["flutter", "typescript", "postgres", "client"]
weight: 4
---

GBL Capital sends trade signals on US index futures (Nasdaq, S&P 500, Dow and Russell) to paying members. The point of the service is a public record of every signal that can't be changed after the fact, so members can check the results for themselves.

I built three parts:

- **Customer app** (Flutter, Android and web). Live signals with entry, stop and targets, push alerts, a contract size calculator, the full public track record with a performance calendar, a personal trade journal, Google sign-in and account recovery.
- **Desk app** for the team. Posting and managing signals, customers, team accounts, notices, maintenance mode and forced updates.
- **Backend** in TypeScript with Fastify and Postgres: a public API, a separate admin API and a background worker. Card billing through Stripe, push notifications through Firebase. About 80 backend tests and 30 app tests, including layout tests at small screen widths and large text sizes.

Paid futures signals to people in the US probably need registration with the CFTC, so the service blocks the US by default until a lawyer confirms the position.

**Status:** apps released as signed Android builds and a web app (2.0.0, October 2026). They run on sample data until the backend is deployed and payments are switched on.

**Site and releases:** [eddyndumia.github.io/gbl-capital-app](https://eddyndumia.github.io/gbl-capital-app/)

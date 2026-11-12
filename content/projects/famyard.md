---
title: "Famyard Enterprises"
summary: "Website and internal business system for a land sales company in Nyeri, Laikipia and Nanyuki, plus the platform for a tokenized land pilot. I'm Head of Technology and Digital Products."
date: 2025-04-29
tags: ["nextjs", "postgres", "hedera", "client"]
weight: 1
---

Famyard sells plots in Nyeri, Laikipia and Nanyuki. Their old site was WordPress and only one person could change anything on it. I rebuilt the site in Next.js and built the system the staff run the business on. My title there is Head of Technology and Digital Products.

**Website.** Estate and plot pages with availability, a map and 360° photos, location guides, a blog, and an enquiry form that feeds the sales team. Every old WordPress link redirects to the right page.

**Internal system.** Each staff member signs in with a role, and each department only sees its own work unless the director allows more. The modules:

- Plots and estates, with an internal price list that only the director sees.
- Enquiries and a sales pipeline from first contact to site visit to sale.
- A payments ledger on each sale, with numbered receipts and a late payments list. Entries can't be edited, only reversed by someone other than the person who recorded them.
- The company email inbox inside the system: read, reply, attach files, and turn an email into an enquiry.
- Notes with mentions, a calendar, live notifications and a security log.
- Two-factor sign-in and encrypted nightly backups.

**Tokenized land pilot.** Famyard plans to put one plot into a company and offer shares of it as tokens through the Capital Markets Authority regulatory sandbox. I built the engine for it as a separate service: investor checks, the holder register, token issuance on the Hedera Token Service, escrow for subscriptions, and reconciliation between the database and the ledger. It runs end to end on Hedera testnet. No investor money is taken until the CMA admits the pilot.

**Stack:** Next.js, Postgres (Neon) with Drizzle, Better Auth, Cloudflare. The pilot engine is TypeScript with Hono, Postgres and the Hedera SDK.

**Live:** [famyard.co.ke](https://famyard.co.ke)

---
title: "Apex AutoMobiles"
summary: "Website and dealer system for a Nairobi car import business. About 1,700 cars listed, with an admin the team uses to run stock, preparation and publishing."
date: 2026-10-27
tags: ["nextjs", "postgres", "cloudflare", "client"]
weight: 2
---

Apex AutoMobiles imports cars into Kenya and sells them from Nairobi, both from the yard and on order. I built the public website and the system the team runs the business from, which they call Apex Manager.

**Website.** Every car has its own page with photos, specs and a price shown as C&F Mombasa, with a switch between shillings and dollars. Buyers can search and filter across the whole stock, browse by make and model, and ask about a car by form, phone or WhatsApp. The site is static pages on Cloudflare, so it loads fast on a phone even with about 1,700 cars listed. Enquiries go to a Cloudflare D1 database and Apex Manager pulls them in every ten minutes.

**Apex Manager.** Staff add and edit cars, manage photos, and track each car on a preparation board, with its tasks and costs, before it can go live. The overview page is a dealer desk showing what needs attention today. When stock changes, a Publish button rebuilds the website through GitHub Actions.

**Moving their old stock over.** The business already had about 1,660 cars on an old WooCommerce site. I wrote an importer that brought every car and its 31,000 photos into the new system, mapped the old fields to the new ones and put everything live at once.

**Stack:** Next.js, Postgres (Neon) with Drizzle and row-level security, Render, Cloudflare Workers, D1 and R2, GitHub Actions.

**Live:** [apex-automobiles.eddyndumia.workers.dev](https://apex-automobiles.eddyndumia.workers.dev)

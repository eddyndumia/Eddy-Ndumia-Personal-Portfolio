---
title: "Capstone — AI Lead Assistant for Real Estate Agents"
summary: "An AI agent that handles WhatsApp and Instagram DMs for real estate agencies — qualifies leads, books viewings, hands off to a human when it should."
date: 2026-09-22
tags: ["ai", "agents", "python", "whatsapp", "real-estate"]
---

Capstone runs the DMs for a real estate agency. A lead messages on WhatsApp or Instagram, the agent qualifies them, answers questions off the agency's own listings, books a viewing, and hands the conversation to a real person the moment it should — a price negotiation, a complaint, anything outside its lane.

An agency owner sets it up through a builder wizard: connect WhatsApp/Instagram, import listings from a spreadsheet (the import is idempotent, so re-uploading an updated sheet never duplicates anything), and the agent is live. There's an inbox where a human can take over any conversation, a leads view, and analytics that track how the agent is doing and what it's costing per client. The agent core isn't hard-locked to real estate either — industry templates exist so the same runtime can be pointed at a different vertical later.

Backend is FastAPI + SQLAlchemy + Postgres. Dashboard is Next.js. Still pre-launch — working toward a first paying pilot rather than a public release. One detail I like: part of the backlog gets worked overnight by an autonomous "night shift" runner — a Claude Code session that picks up the top item, ships what it can inside a fixed window, and leaves a report for the next morning.

**Tech stack:** Python (FastAPI, SQLAlchemy, Postgres), Next.js

**Repo:** [capstone](https://github.com/eddyndumia/capstone) *(private)*

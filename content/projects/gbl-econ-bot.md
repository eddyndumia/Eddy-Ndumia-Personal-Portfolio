---
title: "GBL SuperTrading Bot"
summary: "Discord bot that posts a filtered weekly economic calendar to a trading community, on a schedule."
date: 2026-05-18
tags: ["javascript", "node", "trading", "discord"]
---

A Discord bot for the GBL SuperTrading community — it pulls ForexFactory's weekly economic calendar, filters it down by currency and impact (high/medium/low), and posts the digest to a channel on a cron schedule instead of everyone checking the calendar site themselves. Each weekday carries its own rule ("Trade Day — wait for the 9:30am open", etc.) so the post doubles as a quick reminder, not just a data dump. Slash commands let a mod adjust which currencies, which impact level, the schedule, and the timezone without touching code. Runs alongside a landing page for the same signals-and-community offer.

**Tech stack:** Node.js, discord.js, node-cron

**Repo:** [GBL-Econ-Bot](https://github.com/eddyndumia/GBL-Econ-Bot)

---
title: "GBL SuperTrading Bot"
summary: "Discord bot that posts a filtered weekly economic calendar to a trading community."
date: 2026-05-18
tags: ["javascript", "node", "trading", "discord"]
---

Built for the GBL SuperTrading community. It pulls ForexFactory's weekly calendar, filters it by currency and impact, and posts the digest to a channel on a schedule, so nobody has to check the site. Each weekday carries its own trading rule, so the post doubles as a reminder. Mods change currencies, impact level, schedule and timezone with slash commands, no code.

**Stack:** Node.js, discord.js, node-cron

**Repo:** [GBL-Econ-Bot](https://github.com/eddyndumia/GBL-Econ-Bot)

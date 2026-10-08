---
title: "Chukua"
summary: "Free things from people near you in Nairobi. Live on Android since October 2026."
date: 2026-10-01
tags: ["flutter", "supabase", "postgis", "m-pesa"]
weight: 1
---

Chukua means "take" in Swahili. People list things they don't need, a sofa, a cot, a microwave, and someone nearby claims it and picks it up. The feed shows what's within 5 km with a rough value on each item, so you know if the trip is worth it.

You set where you're looking from a chip at the top of the feed, by GPS or by dragging a pin on the map, and givers set the pickup spot the same way. Once a claim is confirmed the taker gets directions in Google Maps and an "On my way" button so the giver knows they're coming. The account page works like a Google account: photo, sign-in with an email code or Google, and your data to download or delete.

It's Flutter on Supabase, with PostGIS for distance. The rules live in SQL, not the app: one hold at a time, three open claims, twenty listings a day, strikes for no-shows, listings that expire on the giver's date. Row-Level Security keeps the giver's number and exact spot hidden until someone has claimed. Nearby alerts (switching on in the next update) come from Postgres triggers calling an Edge Function that sends through Firebase, so they arrive even with the app closed. English and Swahili, and the Android download is 21 MB.

Claims will cost a small M-Pesa fee so people only claim what they'll pick up. During the pilot they're free.

**Status:** live, v1.1.0, Android.

**Download:** [chukua.chukua.workers.dev](https://chukua.chukua.workers.dev)

**Why I built it:** [Nairobi Is Full of Free Stuff. Nobody Can Find It.](../../posts/nairobi-is-full-of-free-stuff-nobody-can-find/)

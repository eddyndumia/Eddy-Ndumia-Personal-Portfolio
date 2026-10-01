---
title: "Chukua"
summary: "Free things from people near you in Nairobi. Live on Android since October 2026."
date: 2026-10-01
tags: ["flutter", "supabase", "postgis", "m-pesa"]
weight: 1
---

Chukua means "take" in Swahili. People who have things they don't need, a sofa, a cot, a microwave, list them for free, and people nearby claim them and arrange their own pickup. The feed shows what's within 5 km with a rough value on each item, so you know if the trip is worth it.

It's a Flutter app on a Supabase backend with PostGIS for distance. All the rules live in SQL, not in the app: one person holding an item at a time, three open claims max, twenty listings a day, strikes for no-shows, listings that expire on the giver's date. Row-Level Security keeps the giver's phone number and exact spot hidden until someone has claimed. Sign-in is a 6-digit code by email, and it works in English and Swahili.

Claims will cost a small M-Pesa fee so people only claim what they'll actually pick up. For the pilot claims are free.

**Status:** live as a first release, v1.0.0 (October 2026), Android.

**Download:** [chukua.ndumiaeddy8.workers.dev](https://chukua.ndumiaeddy8.workers.dev)

**Why I built it:** [Nairobi Is Full of Free Stuff. Nobody Can Find It.](../../posts/nairobi-is-full-of-free-stuff-nobody-can-find/)

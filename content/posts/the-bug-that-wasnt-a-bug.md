---
title: "The Bug That Wasn't a Bug"
date: 2026-09-25
---

So this happened while I was building the PesaScore backend. A registered profile's name kept reverting to null. Just, randomly. I'd set it, refresh, it's there, come back an hour later, it's gone. No error, no crash, nothing in the logs pointing at it. Classic "this makes no sense" bug.

First thing I did, obviously, blamed the database. Spent like an hour checking writes, checking the query, adding print statements everywhere like a caveman. Nothing. The write was fine. The value was actually getting set. It just... wasn't there later.

Turns out it had nothing to do with the database at all. The dev server's auto-reload was watching the entire project directory, and every time literally any file changed — including a throwaway debug script I'd created and deleted five minutes earlier to test something unrelated — it silently restarted the whole worker. Which wiped all my in-memory state back to defaults. Which looked, from the outside, exactly like a data bug. A registered name reverting to null isn't a symptom of "the reload restarted the process," it's a symptom of "the database forgot," until you actually go read the reload log and realize oh. oh no. it's been restarting this whole time.

I do not know how long I would've kept debugging the wrong layer if I hadn't scrolled up in the terminal out of pure desperation. Days, probably. The actual fix took two minutes. The finding-it took an evening.

Anyway. Moving debug scripts out of the watched directory now. Learned that one the expensive way.

---
title: "The Bug That Wasn't a Bug"
date: 2026-09-25
---

So this happened while I was building the PesaScore backend. A registered profile's name kept reverting to null. Just, randomly. I'd set it, refresh, it's there, come back an hour later, it's gone. No error, no crash, nothing in the logs pointing at it. Classic "this makes no sense" bug.

If you've written software for any amount of time you know this kind. Not the bug that crashes loudly and tells you exactly which line. The quiet one. The one that only happens sometimes, that you can't reproduce when you try, that makes you doubt things you were sure of an hour ago. Those are the ones that eat whole evenings.

First thing I did, obviously, blamed the database. Spent like an hour checking writes, checking the query, adding print statements everywhere like a caveman. Nothing. The write was fine. The value was actually getting set. It just... wasn't there later.

Then I blamed the frontend. Maybe it was sending an empty name on some request I didn't know about. Checked every call. Nothing. Then caching. Nothing again. Every layer I checked was doing exactly what it was supposed to do, and the name still kept disappearing.

Turns out it had nothing to do with any of that. The dev server's auto-reload was watching the entire project directory. Every time literally any file changed, including a throwaway debug script I'd created and deleted five minutes earlier to test something unrelated, it silently restarted the whole worker. That wiped all my in-memory state back to defaults.

From the outside that looked exactly like a data bug. A registered name reverting to null doesn't look like "the reload restarted the process." It looks like "the database forgot." Until you actually go read the reload log and realize oh. oh no. it's been restarting this whole time.

I do not know how long I would've kept debugging the wrong layer if I hadn't scrolled up in the terminal out of pure desperation. Days, probably. The actual fix took two minutes. The finding it took an evening.

A few things I took from it, and actually use now:

Check the boring layer first. The dev server, the environment, what's running and when it restarted. It's never the interesting part of the system, so it's never where you look first, and that's exactly why it's where these bugs hide.

Read the whole terminal. Not the last line, the whole thing. The answer was sitting a few screens up the entire time.

Keep scratch files out of the project. Debug scripts, test data, one-off experiments go in their own folder that nothing is watching.

Don't trust in-memory state while developing. If something important only lives in memory, assume it can vanish any second, because it can.

When every layer looks fine, the problem is between the layers. The database was fine, the API was fine, the frontend was fine. The bug was in how they were being run, not in any of them.

I'm not going to pretend I'll never do this again. I will. Every developer I know has a story like this and most of them have several. The point isn't to never fall for it, it's to fall for it for a shorter time each round.

Anyway. Moving debug scripts out of the watched directory now. Learned that one the expensive way.

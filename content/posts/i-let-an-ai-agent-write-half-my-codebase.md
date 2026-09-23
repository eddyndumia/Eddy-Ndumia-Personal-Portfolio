---
title: "I Let an AI Agent Write Half My Codebase, Ask Me Anything"
date: 2026-09-17
---

Part of Capstone's backlog gets worked overnight by an actual autonomous coding session while I'm asleep. It reads the backlog, picks the top item, ships what it can, commits, and writes me a report. I wake up, read the report with coffee, and decide what to merge. That sentence would've sounded insane to me two years ago and now it's just Tuesday.

If you're not in this world, it's hard to explain how fast it moved. Not long ago AI in coding meant autocomplete that guessed the end of your line. Then it was a chat window you pasted errors into. Now it's something that can take a task, read the codebase, write the code, run the tests and tell you what it did. A lot of developers I know are either all in on it or refuse to touch it, and very few are somewhere in the middle.

Ngl the first few times felt weird. Like I was cheating somehow, or outsourcing the "real" work. Then I noticed the actual bottleneck in building anything was never typing speed. It was decision fatigue. Should this endpoint return this shape or that shape, should the retry logic live here or there, a hundred small calls a day that add up to nothing memorable but eat your whole brain. Having something else grind through the mechanical parts of that, while I still make the calls that actually matter, freed up more than I expected.

Here's how it actually works, as simple as I can put it.

I keep a backlog in the repo, a plain list of what needs doing, in order. At night a session starts on its own, reads the list and picks the top item. It works on it, runs the tests, and commits to a branch, never straight to main. Then it writes a short report. What it did, what it tried that didn't work, what it's unsure about. In the morning I read that report before I read any code, and then I decide what gets merged and what gets thrown away.

A few rules I care about, because without them this is just letting a robot push to production:

Nothing merges without me reading it. The session can commit, it can't ship. Every change goes through the same review I'd give a new developer on their first week.

The report matters more than the code. If it can't explain clearly what it did and why, I don't merge it, even if the tests pass.

It doesn't get the decisions that need context. Anything about pricing, how customers are treated, what data we keep, stays with me. It wasn't in the room for the conversation that explained why the business works this specific weird way, and it can't guess its way there.

No paid surprises. It works inside limits I set, and anything that would cost money or touch real customer data waits for a human.

Doesn't mean it's magic. It gets things wrong constantly, confidently, in ways that would've shipped straight to production if I wasn't checking. It'll write a test that passes because it tests the wrong thing. It'll fix a bug in a way that quietly breaks something two files over. And reading a report every morning instead of just doing the work myself means I have to actually understand what happened, instead of vibing on "yeah looks fine."

Am I still an engineer if half the diff wasn't typed by me. Honestly I think that question ages out fast. Nobody asks a carpenter if they're still a carpenter because they use a power drill. Give it a year, this whole debate is going to sound as dated as arguing over whether using Stack Overflow counts as cheating.

For someone building on no budget, this is the real point. I don't have a team. I can't hire five developers. What I have is my own judgement and a few good hours a day. If a tool can take the mechanical work off those hours, that's the difference between shipping in a month and shipping never.

What actually matters is whether the thing works, whether the customer's problem gets solved, and whether I understood it well enough to be responsible for it. The rest is just tooling.

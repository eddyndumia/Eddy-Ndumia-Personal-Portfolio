---
title: "What Am I Actually Building When I Build an Agent"
date: 2026-09-20
---

Working on Capstone has put me in this genuinely strange spot where I spend my days designing something that talks to people on my behalf. Not a form. Not a script that runs once and dies quietly in a log file. Something that holds a conversation, decides what to say next, remembers what happened three messages ago even when I, personally, have already forgotten. And every so often I stop mid-implementation, hands still on the keyboard, and just think: hold on. What is this. What am I actually doing right now.

I don't mean that in the sci-fi, "is it alive" sense. I am not losing sleep over the WhatsApp bot achieving consciousness. I mean it in the smaller, weirder, much more mundane sense — I am, for a living, encoding *judgment* into a system that will make small decisions when I am nowhere near the room. That used to be a thing you only trusted to another human. A teller, a receptionist, someone you hired, trained, vetted, and hoped would represent you decently on their worst day. Now it's a system prompt and a few hundred lines of orchestration logic, and somehow it still has to represent a business well enough that a stranger texting on WhatsApp at 9pm can't tell — or more accurately, doesn't care — that there's no one actually home in the way there used to be.

## the two easy lies

There are two easy stories to tell yourself here and I don't trust either one. One is "we're building the future of work," delivered with a straight face, which — sure, maybe, but that sentence has never fixed a single bug for me. The other is "relax, it's just autocomplete with extra steps," which is the kind of thing you say right before you ship something careless. What I actually feel, on the days I'm honest about it, is closer to *responsibility*. Plain, unglamorous responsibility. If I build this carelessly, it fails someone quietly, at 11pm, when a real customer needed a real answer and got a confident wrong one instead. That's not a thought experiment I read in a newsletter. That's a design decision I'm making every single week — how much is the agent allowed to guess, versus how often does it have to say "let me get you an actual person"?

Maybe the honest philosophical takeaway here is smaller than I'd like it to be, and I've made peace with that. Building something that *acts* doesn't make me a creator in some grand mythic sense. It mostly just makes me someone who has to think a lot harder about defaults. What does it do when it doesn't know? What does it do when it's confidently wrong? Those used to be questions for a manager writing a training manual in a back office somewhere. Now they're mine, at a terminal, at whatever unreasonable hour I happen to be debugging in.

I don't have a grand unified theory of AI agency to hand you. I just know the weight of the thing is real, even when the thing itself is, mechanically, just Python and a prompt and a WhatsApp webhook that I'm still slightly afraid of.

---
title: "What Am I Actually Building When I Build an Agent"
date: 2026-09-20
---

Working on Capstone means I spend my days building something that talks to people for me. Not a form. Not a script that runs once and dies. Something that holds a conversation, decides what to say next, and remembers what happened a few messages back even when I've already forgotten.

The first thing we're building with it is a WhatsApp support agent for small businesses. Here that makes a lot of sense. A huge amount of business in Kenya already happens on WhatsApp. Customers message the shop to ask if something is in stock, what it costs, whether they deliver to Rongai, if they're open on Sunday. The owner answers between serving people in person, late at night, on the matatu home. Messages pile up, some never get answered, and every unanswered message is a customer who went to the next shop.

So the idea is simple. An agent that answers those messages the way the owner would, any time of day, and hands over to a real person when it should.

Every so often I stop mid-build and just think, wait, what is this actually. Not the sci-fi version, I'm not losing sleep over it waking up. I mean it in the small way. I'm encoding judgment into something that makes decisions when I'm not in the room. That used to be a job you only gave another person, someone you hired and trained and hoped would represent you decently on their worst day. Now it's a prompt and some orchestration code, and it still has to represent a real business well enough that someone messaging on WhatsApp at 9pm doesn't notice, or doesn't care, that there's no one actually home.

Here's roughly how it works. A message comes in through WhatsApp. The agent reads it along with the recent conversation and what it knows about that business, its products, prices, hours, delivery areas. It decides whether it can answer. If it can, it replies. If it can't, or if the customer is upset, or if it's about money in a way it shouldn't touch, it says so and passes the conversation to a person.

A few things I care about getting right, because without them this is just a chatbot that annoys people:

It has to know when it doesn't know. A confident wrong answer is worse than no answer. If a customer asks about a price the agent isn't sure of, it should say let me confirm, not make one up.

Handing over has to be easy. The owner should see the conversation, jump in, and the customer shouldn't have to repeat themselves.

It speaks like the business, not like a robot. Plain words, the way people actually text here, in English or Swahili depending on who's messaging.

Every business is separate. What one shop's agent knows never leaks into another's.

The easy thing is to tell yourself this is just the future of work, or the opposite, that it's just autocomplete with extra steps. I don't fully buy either. What I actually feel, most days, is closer to responsibility. If I build it carelessly, it fails someone quietly, at night, when they needed a real answer and got a confident wrong one instead. That's not a hypothetical. That's a decision I make every week, how much the agent is allowed to guess versus when it has to say let me get you a real person.

I'm not going to pretend this is solved. Models still get things wrong in ways that are hard to predict. WhatsApp has its own rules about what businesses can send and when. Small business owners are busy and skeptical, and fair enough, they've been sold a lot of tools that didn't work. And the agent is only as good as what the business tells it, which means a lot of the work is actually helping owners write down things that have only ever lived in their heads.

I don't have some big theory about AI and agency to hand anyone. I just know the weight of it is real, even though the thing itself is mechanically just Python and a prompt and a webhook I'm still a little scared of.

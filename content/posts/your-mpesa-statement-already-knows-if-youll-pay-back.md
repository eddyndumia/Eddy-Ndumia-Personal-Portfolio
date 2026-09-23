---
title: "Your M-Pesa Statement Already Knows If You'll Pay Back"
date: 2026-09-23T12:00:00+03:00
---

A friend of mine runs a small hardware shop in Kitengela. Cement, iron sheets, paint, the usual. Business is steady, he pays his SACCO every month without missing, he's been doing it for years. Last year he tried to get a proper loan from a bank to stock up before the building season and got turned down. No credit history. The man has moved millions of shillings through his phone and as far as the bank was concerned he didn't exist.

He ended up doing what everyone does. A bit of Fuliza here, a mobile loan there, a chama contribution he borrowed back against. Expensive money, short terms, and none of it helped him look any better to the bank next time.

This is normal in Kenya. Most adults here have never had a bank loan, so the credit bureaus have almost nothing on them, and a lot of what they do have is negative. A few years ago millions of people got listed on CRBs over small digital loans, some over a few hundred shillings, and it followed them around for years. So for a huge part of the country the formal credit record is either empty or it's a punishment.

But these same people have a very detailed financial record. It's just not at a bank. It's on M-Pesa.

Think about what a year of M-Pesa statements actually shows. When your salary lands and whether it lands on the same day every month. Whether you pay your SACCO or your Tala loan on time or whether it bounces. How often you're on Fuliza and whether it's two days before payday or basically every day. Whether anything goes into M-Shwari or it all goes out as fast as it comes in. It's more honest than most bank statements, because people don't dress it up. It's just their life.

Lenders here know this. The big digital lenders were built on phone data. But for most SACCOs and small lenders, reading someone's M-Pesa statement still means a loan officer scrolling through a PDF with thousands of lines and making a judgement call. It's slow, it's inconsistent, and it depends a lot on who is reading.

That's the gap I kept coming back to. The data exists, the borrower already has it, and nobody has made it easy for them to use it in their own favour.

So I built something for it. It's called PesaScore.

Pesa because it's about money, and because most people here say pesa before they say money anyway. It started out as ScoreWise, then I found out there's already an app with that name live in Nigeria doing something different, so I changed it. Honestly PesaScore fits better.

Here's how it works, as simple as I can put it.

You download your M-Pesa statement from the M-PESA app or by dialling the USSD code, same way you would for a loan application. You open PesaScore and upload it. If it's password protected, and Safaricom's usually are, you type the password. The PDF gets read on our server, in memory, and thrown away. It's never saved.

PesaScore goes through every transaction and sorts it. SACCO and lender repayments, Fuliza, savings, everything else. Where it can't tell, it asks you. The best example is bank paybills. If you pay Equity every month, that could be a loan, a savings transfer or your cousin's school fees, and your statement can't tell the difference. So instead of guessing, the app shows you the bank and asks if those were loan repayments. You answer and it moves on.

Then you get a score between 300 and 850, the same range people know from credit scores elsewhere, and under it the three things that built it. How reliably you repay. How much you lean on Fuliza. How much you save compared to what comes in. Each one comes with a plain explanation of why it's where it is and what would move it. There's a simulator where you can see what happens if you cut Fuliza by ten days or save an extra five thousand a month.

On the other side there's a dashboard for lenders. A SACCO asks for your score, you get a request on your phone saying who is asking and exactly what they'll see, and you say yes or no. If you say yes they see your score and only the parts you agreed to share, for a set time, and you can pull it back whenever you want. They can't see your transactions. Each lender only ever sees their own applicants, and that's enforced in the database itself, not just hidden in the app.

A few things I care about getting right, because without them this is just another app harvesting people's data:

The score belongs to the borrower. They upload it, they see it first, they decide who else sees it. A lender can't pull your data without you tapping yes.

The statement is thrown away after it's read. We keep the numbers the score needs and nothing else. I don't want to be sitting on thousands of people's full transaction histories, that's a liability, not an asset.

Every score comes with its reasons. If you get 580 you should know exactly why, and what to do about it. A number with no explanation is just another way of saying no.

It asks instead of guessing. The first version of the parser flagged 63 different businesses as possible loan repayments on a real statement, including Spotify, KPLC and Kenya Airways. Nobody should be asked whether Kenya Airways is a loan. I cut it down to banks and lenders, which brought it to nine. Getting that right mattered more to me than any clever feature.

No scraping. Everything comes from the statement the borrower chooses to upload. There are shortcuts that involve pulling data people didn't knowingly hand over, and I'm not building on any of them.

What this changes, if it works, is a small thing in one way. My friend in Kitengela walks into a SACCO or a bank with a score that actually reflects how he runs his money, instead of a blank file. For the lender it means ten minutes of scrolling a PDF becomes a few seconds, and two loan officers looking at the same person get the same answer. And for the people who got burned by CRB listings over small loans, it's a way to show the rest of the picture, the years of paying things on time that the bureau never saw.

I'm not going to pretend this is easy. There's a lot that isn't done.

The score right now is a set of rules I wrote, not a trained model. Repayments count for half, savings for thirty percent, Fuliza for twenty. I picked those weights on purpose and I can explain every one of them, but they haven't been tested against what real borrowers actually did. To do that properly you need loan outcomes, who paid back and who didn't, and only lenders have that. That's the next big step and I can't do it alone.

M-Pesa can show whether a payment went through, but not whether it was late, because it doesn't know when it was due. The parser has been tested on one real statement, a two-year one with about 7,400 transactions, plus synthetic ones I generate for demos. That's not enough. I need to see a lot more statements from a lot more kinds of people before I trust it on everyone. There's no automated test suite yet. And there's the regulatory side, the Data Protection Act, registering with the Data Commissioner, and working out exactly where a scoring service sits with the CRB rules. None of that is optional in fintech and I'd rather sort it early than get surprised.

So the plan is small on purpose. Get it in front of a few SACCOs and lenders who already look at M-Pesa statements by hand. Run PesaScore next to their loan officers for a while, not instead of them, and compare. When the loans from that period either get paid or don't, use that to fix the weights and find out which of the other signals I've been playing with actually matter. Things like how regular your salary is and how many different places you spend. I compute them already, they're just not in the score, because I'm not adding anything I can't back up.

Building from Nairobi means you notice things like this because you live them. Everyone here knows someone who is good with money and still can't get a loan, and everyone knows the M-Pesa statement is where the truth is. It's just been sitting there as a PDF nobody reads properly.

The data is already on everyone's phone. I just want people to be able to use it for themselves.

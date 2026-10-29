---
title: "Why Most AI Covers Sound Like Slop"
date: 2026-10-29T08:00:00+03:00
---

You've heard one. You're scrolling TikTok or YouTube Shorts and there's Drake singing a Sauti Sol song, or Juice WRLD doing some Afrobeats track that came out last month. For about five seconds it's funny. Then you actually listen. The voice sounds a bit metallic, like it's coming through a tin. On the high notes it cracks into a robot. The original singer is still faintly there in the background doing the harmonies. The vocal sits on top of the beat like a sticker instead of inside it. And there's this smeared reverb on everything, like the whole song was recorded in a bathroom.

That's most AI covers right now. People call it slop and honestly that's fair.

The thing is the tools to make these are free. Suno will write you a full song from a sentence. Hugging Face has voice models of basically every artist alive, hundreds of them, made by fans. RVC, the voice conversion model almost everyone uses, is open source and runs on a normal PC. So anyone can make a cover in an afternoon, and a lot of people do, and most of them sound the same kind of bad.

I got into this because I wanted to make covers for fun and mine sounded bad too. So I started digging into why. And what I found is that the voice model is maybe a third of it. The rest is everything that happens before and after the model, and that's the part almost nobody does properly, because it's boring audio engineering and not AI.

Here's what actually goes wrong.

First the separation. To put a new voice on a song you have to pull the vocal out of the finished track. Most people use whatever splitter came with the tool, and those leave bits of the beat in the vocal and bits of the vocal in the beat. Then the voice model tries to convert hi-hats and snare into Drake, and that's where a lot of the metallic sound comes from. On top of that a song has a lead vocal and backing vocals, the harmonies and ad-libs. If you don't split those apart the model gets three voices at once and makes a mess, or you leave the backing in the original voice and that's the ghost you hear in the background.

Then reverb. The vocal you pulled out already has the original song's reverb baked in. Convert that and you get the bathroom sound, because the model is trying to copy the echo too.

Then the mix. Most covers just put the converted vocal back on the beat at whatever volume it came out at. No EQ, no compression, nothing taming the harsh S sounds, no reverb that matches the song. In a real song the vocal and the beat are mixed to fit each other. The beat dips a little when the singer comes in, the vocal is compressed so it sits at one level, there's space carved out for it. Skip all that and it sounds like karaoke.

And the last one is the performance underneath. A voice model copies the tone of a voice, it doesn't sing for you. It keeps the timing, the phrasing, the breaths, the little runs of whatever vocal you fed it. If you feed it a Suno vocal, which is already a bit lifeless, you get a lifeless Drake. If you feed it a real person singing with feeling, you get something that actually sounds like a performance. This is the one most people skip completely.

So none of the slop is really the AI's fault. It's what happens when you take one good model and skip every step around it.

That's what I built. It's called Voice Forge. It's a Windows desktop app, and the name is just what it does, you forge a song into a new voice.

Here's how it works, as simple as I can put it.

You give it a song. A Suno link, any audio file, or you record yourself singing over a beat right inside the app. You pick a voice. Then it does the whole chain. It splits the vocal from the beat with a much better separation model, BS-Roformer, which is close to the best one available right now. Then it splits the lead vocal from the backing vocals with a second model. Then it takes the reverb off the lead. Then it works out the pitch, comparing how high the original singer sings with how high the voice you picked usually sings, and shifts it in whole octaves so it stays in the song's key. Then it converts the lead with RVC, or with Seed-VC which is newer and sometimes better. You can choose to convert the backing vocals too, so there's no ghost of the old singer.

Then the mix. I spent more time on this part than anything else. The vocal goes through a proper chain built on Spotify's open source audio library, pedalboard. EQ, compression, a de-esser for the harsh S sounds. The vocal level gets set relative to the beat, copied from how loud the vocal was in the original song, so it sits where the original producer put it. The beat dips a tiny bit under the vocal, there's reverb and a delay timed to the song's tempo, and then it's mastered to a normal streaming loudness. If you have a finished song whose sound you like, you can give it as a reference and a tool called Matchering masters yours to match it.

The heavy part, the separation and the conversion, runs on a GPU. I don't have one. My laptop has an Intel chip with built-in graphics and that's it. So the app uses Kaggle. Kaggle is Google's data science site and it gives every account about 30 hours a week on an Nvidia T4 GPU for free, for notebooks. The app talks to Kaggle through its API. It uploads your song as a private dataset, pushes a private script that does the work, waits for it, and downloads the result. You never open Kaggle. On the free hours that's a lot of songs a week. There's also a Standard mode that runs everything on the PC, slower and a bit lower quality, for when you don't want to wait for Kaggle.

There's some other stuff in there. You can write lyrics and a style and it makes a full song with ACE-Step, an open source music model, also on Kaggle. You can export a 30 second vertical video of any song for Shorts or TikTok. There's a player with an equalizer, and I've been redesigning every screen in it recently, new logo, a splash screen, the whole thing. And there's a wizard to train a voice model of your own voice from recordings, which also runs on Kaggle.

A few things I care about getting right.

The performance comes first. That's why the record tab exists. You sing over the beat, you can do as many takes as you want, it calibrates for the delay in your headphones, and then your take goes through the same chain. A real person singing badly into a cheap mic and converted properly sounds more real than a perfect AI vocal converted badly. I didn't expect that but it's true every time.

Celebrity voices stay on your PC. You can download any artist's voice model and use it, that's on you and it's your computer. But I'm not building a site where people post songs in Drake's voice. Every voice in the app has a license on it, personal, your own, or licensed with permission. Only your own voice or a voice someone gave you permission for can be published. The app checks it and the server checks it again.

Training your own voice needs consent from the person whose voice it is. The wizard asks the person to read a sentence out loud, their name, what the voice is for, the date, and that recording gets saved with the model. It's a small thing but it means there's a record that this person actually agreed.

Everything published is labelled AI generated. Every file the app exports has it in the metadata too. People should know what they're listening to.

It should cost nothing to run. No paid APIs, no servers I'm paying for. The GPU is free Kaggle hours, the models are all open source, and the community site runs on Cloudflare's free tier.

That community site is the other half. It's called Voice Forge Online. People sign in with Google, publish songs made with their own voices, follow each other, like and comment, the usual. The app signs in through the browser so you never type a password into it. It's built and it works locally but it's not deployed yet.

I'm not going to pretend this is easy. There's a lot that can go wrong.

Voice cloning is a legal grey area almost everywhere, and the music industry is suing AI companies already. Keeping artist voices local and only allowing own or licensed voices online is my answer for now, but I'd want a proper legal read before the site goes public. Kaggle's free GPUs are free until they aren't, and if they change the rules the Studio Quality mode needs another home. Moderation on any site where people upload audio is real work, there's a report button and a copyright form already but someone has to actually read them. And RVC still has artifacts. A good chain hides most of them, not all of them. Some voice models are just bad and nothing fixes that.

So the plan is small. Finish the redesign that's going on now. Use it myself for a while and make covers until the rough edges stop showing up. Then deploy the site, and maybe put out a download if people actually want one.

For now it's a tool I use, and it makes covers that don't sound like a tin can.

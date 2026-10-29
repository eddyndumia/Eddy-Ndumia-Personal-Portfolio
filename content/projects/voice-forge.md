---
title: "Voice Forge"
summary: "Windows desktop app that re-sings a song, or your own recorded vocal, in another voice and mixes and masters it. Heavy GPU work runs on free Kaggle T4s. In development."
date: 2026-10-29
tags: ["python", "audio", "kaggle", "cloudflare"]
weight: 4
---

You paste a Suno link, drop in a song, or record your own vocal over a beat inside the app. Voice Forge separates the vocal from the instrumental, re-sings it in the voice you picked, and mixes and masters it back over the beat.

The separation is BS-Roformer for vocals and instrumental, then a second model that splits the lead from the backing vocals, then de-reverb on the lead. The conversion is RVC through Applio, or Seed-VC. Pitch can be picked automatically from the source vocal and the voice's usual range, in whole octaves so it stays in key. The mix is a real chain built on Spotify's pedalboard: EQ, compression, de-esser, the vocal level set against the beat the way the original song had it, the beat ducking slightly under the vocal, reverb and delay, a limiter. If you give it a finished song you like, Matchering masters yours to match it.

The heavy part runs on a free Kaggle T4 GPU. The app uploads the inputs as private Kaggle datasets, pushes a private script, waits for it and downloads the stems. Kaggle gives about 30 GPU hours a week for free, which is a lot of songs. There's a Standard mode that runs on the PC too, with the splitter on the Intel iGPU through DirectML.

Other parts: lyrics to a full song with ACE-Step 1.5 on Kaggle, a Shorts video export, a 10 band equalizer in the player, and a wizard to train a voice model of your own voice, with a recorded consent step from the person whose voice it is.

Every voice has a license in a small registry. Voices of real artists stay personal and on your own PC. Only your own voice or a voice you have permission for can be published to Voice Forge Online, a community site on Cloudflare Workers, D1 and R2 with Google sign-in. The site is built but not deployed yet.

**Status:** in development, private, no download yet.

**Stack:** Python, FastAPI, pywebview, PyTorch, ONNX Runtime (DirectML), Applio RVC, pedalboard, Matchering, Kaggle API, Cloudflare Workers, D1, R2

**The story:** [Why Most AI Covers Sound Like Slop](../../posts/why-most-ai-covers-sound-like-slop/)

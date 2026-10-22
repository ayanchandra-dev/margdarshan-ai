# Margdarshan AI

**A voice-first agent that finds live training and job opportunities, then helps people apply.**

Built for Kritical Hacks 2026 (AI/ML Track, Student category).

## The problem

Skilling programmes train millions of people, but many never reach a livelihood.

- PMKVY 2.0 short-term training: 33.6 lakh trained, 15.3 lakh reported placed (45.6%). Source: NSDC.
- Younger trainees were placed least often: 33% for ages 14-18. Source: NSDC, PMKVY STT Program Analytics, Nov 2020.
- Trained people earned 15% more per month than a comparison group, so getting people to the right training pays off. Source: MSDE reply in Rajya Sabha, 2022.

People with low literacy often cannot navigate text-heavy forms and portals. They get no personalised guidance, and opportunity information is scattered and goes out of date.

## The solution

1. **Speak:** the user talks in their own language. No typing, no forms.
2. **Understand:** AI builds a profile: education, skills, interests, location and constraints.
3. **Match:** finds the skill gap and ranks NSQF-aligned courses and pathways.
4. **Find live:** TinyFish searches live portals for open batches, jobs and apprenticeships nearby.
5. **Apply:** an agent pre-fills the registration. The user confirms before anything is submitted.

This is not a chatbot over a static dataset. It works on the live web and takes action for people who cannot navigate portals themselves.

## Architecture

Voice in (Indic STT) -> LLM agent (intent and profile extraction) -> Matcher (skill gap and NSQF ranking) -> TinyFish live web layer -> Voice out (Indic TTS, WhatsApp, web)

## TinyFish integration

| TinyFish API | How Margdarshan AI uses it |
|---|---|
| Search API | Finds current training batches, openings, apprenticeships and scheme pages for the user's profile and district |
| Fetch API | Renders chosen portal pages and extracts clean content: eligibility, dates, centre address, documents needed |
| Agent API | Works through a real website from a plain-language goal, used to pre-fill registrations and applications |

If a portal is unreachable, cached results are shown with their date.

## Tech stack

Next.js, FastAPI, PostgreSQL, Whisper / Indic STT, Indic TTS, TinyFish APIs.

## Demo scope (24-hour build)

- Hindi voice input with a text fallback
- One district's live training and job listings through TinyFish
- One complete flow: speak, match, find, pre-fill, confirm

## Safety and privacy

- Answers are grounded in fetched pages and carry source links.
- Only data needed for matching is collected. No portal credentials are stored.
- The user gives explicit consent before any submission.

## Future scope

- More Indian languages, WhatsApp voice and IVR for feature phones
- Verified listings from training partners and employers, CSC and district skill office integration
- Anonymised district dashboards showing skill demand and supply gaps

## Status

Concept and architecture submitted for Kritical Hacks 2026. The working build starts at the hackathon. The pitch deck is in this repository.

## References

- NSDC, PMKVY 2.0: Analysis of Sectoral Performance (skillsip.nsdcindia.org)
- NSDC, PMKVY STT Program Analytics, November 2020 (skillsip.nsdcindia.org)
- Rajya Sabha unstarred question, 2 Feb 2022 (rsdebate.nic.in)
- TinyFish documentation (docs.tinyfish.ai)
- PM-AJAY (pmajay.dosje.gov.in) and Skill India Digital (dgt.skillindiadigital.gov.in)

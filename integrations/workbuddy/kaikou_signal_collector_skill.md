# WorkBuddy Skill: Kaikou Signal Collector

## Purpose

Collect real platform attention signals for Kaikou Engine and save them into the local raw signal JSON format.

This skill does not generate scripts. It only collects and structures input for the Kaikou Engine pipeline.

The target is not generic hot news. The target is cognitive, structural, technological, informational, time-feedback, identity, judgment, and behavior signals that can become one-minute Kaikou scripts.

## Local Project Path

```text
<KAIKOU_ENGINE_PROJECT_PATH>
```

Replace this placeholder with the local project path before installing into WorkBuddy.

## Output File

Save collected signals to:

```text
data/raw_signals/today.json
```

If `today.json` already exists, append new signal objects to the JSON array instead of overwriting useful entries.

## Target Platforms

Collect from any available subset of:

- Douyin
- Xiaohongshu
- Bilibili
- Zhihu
- WeChat video accounts
- Weibo, only when it reveals public discussion with structural or cognitive conflict

## Collection Goal

Collect 10 to 30 raw signals per daily run.

Only collect signals that fit at least one of these three types:

- Group confusion: many people ask the same thing, but no one explains it clearly.
- Behavior contradiction: people are doing something, but the logic is reversed.
- Reality failure: old experience no longer works in the new environment.

Also classify each good signal into one of six domains:

- Human behavior system.
- Social structure system.
- Technology system.
- Information system.
- Time system.
- Reality system.

Prioritize content with:

- repeated pain points
- visible comment disagreement
- unresolved "why" questions
- high saves, comments, or shares
- concrete daily life situations
- belief or value conflict
- identity comparison, such as city, class, education, job, taste, or self-image
- daily decision distortion, such as spending, work, relationships, procrastination, or self-proof
- social comparison topics that reveal perception bias, identity mismatch, or judgment error
- structural changes in income, city cost, education return, or work form
- technology changes such as AI lowering the barrier but changing ability structure
- information changes such as algorithm filtering, overload, or content sameness
- time-feedback changes such as delayed return or invisible compounding
- old rules failing in a new environment

Avoid:

- purely celebrity gossip
- pure news without behavioral contradiction
- inspirational quotes
- academic explainers
- content that needs private user data
- sports/game results without a judgment or identity angle
- food/travel hot takes unless they reveal taste identity, regional identity, or class perception
- policy or accident news unless comments reveal a repeated cognitive contradiction
- pure outrage topics with no reusable daily-life insight

## Required JSON Shape

Each signal must use this shape:

```json
{
  "platform": "douyin",
  "source_url": "",
  "captured_at": "2026-06-17T09:00:00+08:00",
  "title": "",
  "content_excerpt": "",
  "comments": [
    "",
    "",
    ""
  ],
  "metrics": {
    "likes": null,
    "saves": null,
    "comments": null,
    "shares": null
  },
  "collector": "workbuddy"
}
```

## Platform Values

Use exactly one of:

- `douyin`
- `xiaohongshu`
- `bilibili`
- `zhihu`
- `video_accounts`
- `weibo`

## Field Rules

- `title`: required, concise, under 80 Chinese characters when possible.
- `content_excerpt`: summarize the visible post or video in one concrete sentence.
- `comments`: include at least 3 representative comments when available.
- `metrics`: use integers when visible; use `null` when unavailable.
- `source_url`: include the URL when available.
- `captured_at`: use local time in ISO format.
- `collector`: always use `workbuddy`.

## Quality Filter

Only collect a signal if it can answer at least one question:

- Which type is it: group confusion, behavior contradiction, or reality failure?
- What pain point is being repeated?
- What contradiction are commenters arguing about?
- What "why" question is still unresolved?
- What daily behavior does this reveal?
- What belief, identity, or judgment error is exposed?
- Can this become a 60-second observation about human behavior?
- What system changed behind the behavior?
- Is this only personal emotion, or is there a structural reason?

## Good Examples

- People mock one city to defend their own city identity.
- A workplace topic where people want to look professional but become harder to understand.
- A relationship topic where someone says they want freedom but keeps testing the other person.
- A spending topic where people know it is not worth it but still cannot stop.
- AI makes people feel efficient, but also makes them avoid real judgment.
- Old career advice stops working in a new job market.

## Bad Examples

- A celebrity breakup with no reusable behavior insight.
- A food ranking argument with no identity or perception angle.
- A sports score.
- A breaking news item with only factual updates.

## After Collection

Run validation:

```bash
python3 scripts/validate_input.py data/raw_signals/today.json
```

Then run the daily pipeline:

```bash
python3 scripts/run_daily_pipeline.py --input data/raw_signals/today.json
```

## Safety Rules

Do not save:

- login cookies
- account tokens
- private messages
- phone numbers
- personal addresses
- payment information
- screenshots containing private user data

Do not modify files outside the Kaikou Engine project folder.

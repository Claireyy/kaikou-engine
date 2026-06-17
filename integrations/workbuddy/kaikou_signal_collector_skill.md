# WorkBuddy Skill: Kaikou Signal Collector

## Purpose

Collect real platform attention signals for Kaikou Engine and save them into the local raw signal JSON format.

This skill does not generate scripts. It only collects and structures input for the Kaikou Engine pipeline.

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

## Collection Goal

Collect 10 to 30 raw signals per daily run.

Prioritize content with:

- repeated pain points
- visible comment disagreement
- unresolved "why" questions
- high saves, comments, or shares
- concrete daily life situations

Avoid:

- purely celebrity gossip
- pure news without behavioral contradiction
- inspirational quotes
- academic explainers
- content that needs private user data

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

- What pain point is being repeated?
- What contradiction are commenters arguing about?
- What "why" question is still unresolved?
- What daily behavior does this reveal?

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

# Data Schema

## Raw Signal

```json
{
  "platform": "douyin",
  "source_url": "",
  "captured_at": "2026-06-17T00:00:00+08:00",
  "title": "",
  "content_excerpt": "",
  "comments": [],
  "metrics": {
    "likes": null,
    "saves": null,
    "comments": null,
    "shares": null
  },
  "collector": "manual"
}
```

## Topic Candidate

```json
{
  "phenomenon": "",
  "cognitive_label": "",
  "model": "",
  "scores": {
    "real_world_frequency": 0,
    "emotional_resonance": 0,
    "cognitive_contradiction_strength": 0,
    "comment_debate_potential": 0,
    "speech_simplicity": 0,
    "total": 0
  },
  "selection_status": "usable"
}
```

## Content Package

```json
{
  "topic": {},
  "script": "",
  "editing_script": [],
  "subtitle_lines": [],
  "publishing": {
    "titles": [],
    "caption": "",
    "hashtags": []
  }
}
```


# WorkBuddy Skill: Kaikou Publish

## Purpose

Run the local Kaikou Engine pipeline, publish the generated scripts to Kaikou, and return the short link to the user.

Use this skill when the user says:

- 生成开口短链接
- 输出到开口
- 跑今天的开口闭环
- 生成今天4条并给我链接

## Local Project Path

```text
<KAIKOU_ENGINE_PROJECT_PATH>
```

Replace this placeholder with the local project path before installing into WorkBuddy.

## Expected Input

WorkBuddy or the user should already have created:

```text
data/raw_signals/today.json
```

This file must contain 10 to 30 valid raw platform signals.

## One-Command Flow

Run this command from the project root:

```bash
python3 scripts/run_and_publish_kaikou.py --input data/raw_signals/today.json --copy
```

## What The Command Does

1. Validates `today.json`.
2. Generates 4 Kaikou scripts.
3. Writes the run folder under `outputs/daily_runs/<timestamp>/`.
4. Creates a Kaikou task link at `https://kaikou-e43.pages.dev/`.
5. Saves the link to `kaikou_link.txt`.
6. Prints the link.
7. Copies the link to clipboard when possible.

## Required Response To User

After running, reply with:

```text
今天的开口短链接：
<link>

输出目录：
<run folder>
```

Do not only say "done". Always provide the link.

## If Something Fails

If validation fails:

- tell the user which input fields are missing
- do not generate scripts

If short-link generation fails:

- provide the fallback long link if available
- still tell the user where `kaikou_link.txt` is saved

## Safety Rules

Do not commit or upload:

- raw signal files
- local history
- private WorkBuddy files
- tokens
- cookies
- screenshots with private data


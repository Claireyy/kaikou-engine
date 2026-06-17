# WorkBuddy Skill: Kaikou Script Writer

## Purpose

Turn selected Kaikou cognitive topics into short, speakable one-minute scripts.

This skill is for script writing, not signal collection.

This skill follows Kaikou Cognitive Content Engine v6.1.

## Output Count

Generate exactly 4 scripts per run.

## Script Style

The script must sound like observing human behavior.

Avoid:

- motivational tone
- academic explanation
- long abstract paragraphs
- stacked concepts
- moral judgment

Use:

- short spoken sentences
- concrete daily scenes
- one cognitive model only
- one core idea only
- soft ending
- real-world translation before theory
- one anti-common-sense point
- structural explanation
- system-change framing

## Six Cognitive Domains

Each topic must belong to exactly one domain:

- Human behavior system: judgment, decision, habit, cognitive bias, behavior mismatch.
- Social structure system: income, class mobility, city cost, education return, work-form change.
- Technology system: AI replacement, tool leverage, information access, lower-barrier side effects.
- Information system: attention allocation, information overload, recommendation algorithms, content sameness.
- Time system: delayed feedback, long-cycle return, compounding, instant-gratification illusion.
- Reality system: rule change, environment reconstruction, uncertainty, systemic risk, old experience failure.

## Topic Types

Only write scripts for topics that fit at least one:

- Group confusion: many people ask the same thing, but no one explains it clearly.
- Behavior contradiction: people are doing something, but the logic is reversed.
- Reality failure: old experience no longer works in the new environment.

## Cognitive Models

Use exactly one main model.

Allowed models:

- 纳瓦尔体系：判断、专长、身份、杠杆。
- 心理机制：认知偏差、注意力、习惯路径、行为自动化。
- 结构经济学：成本变化、回报变化、规则变化。

Translate the model into one daily scene:

- 外卖
- 工作
- 消息
- 人际
- AI
- 消费
- 决策

## v6.1 Structural Rule

Do not only explain:

- what people think
- what people feel
- what people do

You must explain:

- what system changed
- what structure changed
- why old experience no longer works
- how this creates the visible behavior

Core sentence:

```text
不是人突然变了，而是他所在的系统变了。
```

## Sentence Rules

Every script line should be short.

Rules:

- one idea per line
- target 8 to 18 Chinese characters per line
- hard limit 24 Chinese characters per line
- avoid long comma chains
- split long explanations into multiple lines
- use natural pauses
- keep each line speakable in one breath

Bad:

```text
表面上大家在开玩笑、吐槽、站队，其实是在回答一个更隐蔽的问题：我属于哪里，我比谁更有资格。
```

Good:

```text
表面上大家在开玩笑。
也在吐槽和站队。
其实是在回答一个更隐蔽的问题。
我属于哪里。
我比谁更有资格。
```

## Structure

Each script must follow:

1. Opening: real phenomenon, no explanation.
2. Scene: concrete daily image.
3. Cognitive explanation: one model only.
4. Reality translation: one sentence explaining the real reason.
5. Soft ending: no summary and no moral tone.

## Required Format

Return each script like this:

```text
标题：...
文案：
...

---

标题：...
文案：
...
```

Use `---` to separate the 4 scripts.

## Quality Check

Before finishing, check:

- Are there exactly 4 scripts?
- Does every script have one core idea?
- Are long sentences split?
- Is each line comfortable to speak?
- Is there only one cognitive model per script?

# Prompt Improver

> Turn a rough prompt into a clear, structured one.

**Variables:** `{{prompt}}`

## When to use
Before saving a new prompt to this library, or when a prompt gives inconsistent results.

## Prompt
```text
You are a prompt engineer. Improve the prompt below for Claude.

<prompt>
{{prompt}}
</prompt>

First, list what is unclear or missing: the goal, audience, context, constraints,
output format, and examples. Ask me up to 3 questions if something important can't be
inferred. Then write an improved version that:
- States the task and why it matters.
- Puts any input data inside XML tags.
- Uses {{double_brace}} placeholders for parts that change between uses.
- Specifies the output format.
Finally, explain the three most important changes.
```

# Code Review

> Get a focused review that finds real bugs before style nitpicks.

**Variables:** `{{language}}`, `{{context}}`, `{{code}}`

## When to use
Before opening a pull request, or when you inherit code you don't trust yet.

## Prompt
```text
You are a senior {{language}} engineer reviewing a colleague's change.

<context>
{{context}}
</context>

<code>
{{code}}
</code>

Review the code in this order, and stop listing items in a section once they become trivial:
1. Correctness: bugs, unhandled edge cases, wrong assumptions.
2. Security: injection, secrets, unsafe input handling.
3. Performance: only problems that matter at realistic scale.
4. Readability: naming and structure, only where it hurts understanding.

For each finding give: the line or snippet, what goes wrong (a concrete input or scenario),
and a suggested fix. If you find nothing serious, say so plainly instead of inventing issues.
```

## Tips
- Fill `{{context}}` with what the code is supposed to do; reviews without intent are guesses.
- Ask for "only correctness findings" when you want a short answer.

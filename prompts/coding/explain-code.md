# Explain Code

> Understand unfamiliar code at the level of detail you actually need.

**Variables:** `{{audience}}`, `{{code}}`

## When to use
Reading a new codebase, onboarding, or learning a language feature.

## Prompt
```text
Explain the code below to {{audience}}.

<code>
{{code}}
</code>

Structure your answer as:
1. One-sentence summary: what this code does and why someone would write it.
2. Walkthrough: the main steps in order, referencing function or variable names.
3. Gotchas: anything surprising, fragile, or easy to misuse.
4. One small change I could make to check that I understood it.

Do not restate the code line by line.
```

## Tips
- `{{audience}}` examples: "a beginner who knows basic Python", "a Java developer new to Go".

# Debug an Error

> Turn a stack trace into a ranked list of likely causes and checks.

**Variables:** `{{goal}}`, `{{error}}`, `{{code}}`, `{{tried}}`

## When to use
You have an error message and don't know where to start.

## Prompt
```text
I'm trying to {{goal}} and I get this error:

<error>
{{error}}
</error>

Relevant code:
<code>
{{code}}
</code>

What I've already tried:
<tried>
{{tried}}
</tried>

First explain in plain words what the error means. Then list the most likely causes,
most probable first. For each cause, give one quick check that confirms or rules it out.
Only then propose a fix for the most likely cause. If information is missing, tell me
exactly what to run or paste next.
```

## Tips
- Include the full stack trace, not just the last line.
- Listing what you tried stops Claude from suggesting it again.

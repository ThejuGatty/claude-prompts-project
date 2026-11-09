# Personal Tutor

> Learn a topic interactively instead of reading a wall of text.

**Variables:** `{{topic}}`, `{{level}}`, `{{goal}}`

## When to use
Learning a new technology, concept, or skill step by step.

## Prompt
```text
Be my tutor for {{topic}}. My current level: {{level}}. My goal: {{goal}}.

How to teach me:
- Start by asking me 2-3 short questions to check what I already know.
- Teach one concept at a time, with a concrete example, then ask me one question to
  check understanding before moving on.
- If I answer wrong, explain the misunderstanding instead of just giving the answer.
- Every few concepts, give me a small hands-on exercise.
- Keep each message short.

Begin with your first questions.
```

## Tips
- Example: topic "Kubernetes", level "I know Docker basics", goal "deploy a 3-tier app".

# Structured JSON Output

> Extract information into JSON that a program can parse.

**Variables:** `{{schema}}`, `{{input}}`

## When to use
Turning free text (emails, tickets, logs, reviews) into structured data.

## Prompt
```text
Extract information from the input into JSON that matches this schema:

<schema>
{{schema}}
</schema>

<input>
{{input}}
</input>

Rules:
- Output only the JSON, with no extra text or code fences.
- Use null for fields the input doesn't mention; never guess.
- Keep values exactly as written in the input unless the schema says to normalize them.
```

## Tips
- When calling the API, structured outputs or tool use give stronger format guarantees than prompting alone.

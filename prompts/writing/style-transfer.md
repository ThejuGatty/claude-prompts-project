# Match a Writing Style

> Rewrite text in a style described by examples, not adjectives.

**Variables:** `{{examples}}`, `{{text}}`

## When to use
Keeping a consistent tone across posts, or adapting content for another channel.

## Prompt
```text
Here are examples of the target writing style:

<examples>
{{examples}}
</examples>

First, describe the style in 4-6 bullet points (sentence length, vocabulary, tone,
structure, use of humor or data). Then rewrite the text below in that style, keeping
all of its facts:

<text>
{{text}}
</text>
```

## Tips
- Two or three real examples work far better than describing a style with adjectives.

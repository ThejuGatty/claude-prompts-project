# claude-prompts-project

A curated, tested library of prompts for [Claude](https://claude.ai), organized by
category. Each prompt is a reusable template: copy it, replace the `{{variables}}`,
and paste it into Claude.

## How to use a prompt

1. Pick a prompt from the index below.
2. Copy the text inside the **Prompt** block.
3. Replace every `{{variable}}` with your own content.
4. Paste it into Claude (claude.ai, the API, or Claude Code).

## Prompt index

<!-- INDEX:START -->
### Business

| Prompt | What it does |
| --- | --- |
| [Analyze a Decision](prompts/business/decision-analysis.md) | Look at a decision from several angles before committing. |
| [Professional Email](prompts/business/professional-email.md) | Draft a clear email that gets the response you need. |

### Coding

| Prompt | What it does |
| --- | --- |
| [Code Review](prompts/coding/code-review.md) | Get a focused review that finds real bugs before style nitpicks. |
| [Debug an Error](prompts/coding/debug-error.md) | Turn a stack trace into a ranked list of likely causes and checks. |
| [Explain Code](prompts/coding/explain-code.md) | Understand unfamiliar code at the level of detail you actually need. |
| [Write Unit Tests](prompts/coding/write-tests.md) | Generate tests that cover behavior and edge cases, not just the happy path. |

### DevOps

| Prompt | What it does |
| --- | --- |
| [Create a CI Pipeline](prompts/devops/ci-pipeline.md) | Get a working CI workflow for build, test, and (optionally) image publishing. |
| [Write a Dockerfile](prompts/devops/dockerfile.md) | Produce a small, secure, production-ready Dockerfile for an app. |
| [Troubleshoot Infrastructure](prompts/devops/troubleshoot-infra.md) | Work through a broken server, container, or cluster methodically. |

### Learning

| Prompt | What it does |
| --- | --- |
| [Explain Simply](prompts/learning/explain-simply.md) | Get a layered explanation, from one sentence to real depth. |
| [Personal Tutor](prompts/learning/tutor.md) | Learn a topic interactively instead of reading a wall of text. |

### Meta

| Prompt | What it does |
| --- | --- |
| [Prompt Improver](prompts/meta/prompt-improver.md) | Turn a rough prompt into a clear, structured one. |
| [Structured JSON Output](prompts/meta/structured-output.md) | Extract information into JSON that a program can parse. |

### Writing

| Prompt | What it does |
| --- | --- |
| [Expert Editor](prompts/writing/expert-editor.md) | Tighten a draft while keeping your voice. |
| [Match a Writing Style](prompts/writing/style-transfer.md) | Rewrite text in a style described by examples, not adjectives. |
<!-- INDEX:END -->

## Prompting principles used here

- **Be explicit about the goal and audience.** Claude does better when it knows why.
- **Wrap pasted input in XML tags** such as `<code>` or `<text>` so instructions and data stay separate.
- **Specify the output format** (sections, length, JSON) instead of hoping for it.
- **Ask for reasoning before answers** on hard problems (list causes, then fix).
- **Allow "I don't know."** Prompts tell Claude not to invent issues or facts.

## Adding a prompt

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: copy [TEMPLATE.md](TEMPLATE.md) into
the right `prompts/<category>/` folder, then run:

```bash
python scripts/build_index.py
```

## Further reading

- [Anthropic prompt engineering guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Claude Code documentation](https://code.claude.com/docs)
- Inspired by the community collection [langgptai/awesome-claude-prompts](https://github.com/langgptai/awesome-claude-prompts). The prompts here are written independently.

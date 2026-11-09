# CLAUDE.md

A Markdown library of reusable Claude prompts. There is no application code.

## Layout
- `prompts/<category>/<name>.md`: one prompt per file, following `TEMPLATE.md`.
- `scripts/build_index.py`: validates prompt files and regenerates the index in `README.md`
  between `<!-- INDEX:START -->` and `<!-- INDEX:END -->`. Never edit that block by hand.
- `.github/workflows/check.yml`: runs `python scripts/build_index.py --check`.

## When adding or editing prompts
- Follow `TEMPLATE.md` exactly: `# Title`, `> summary`, `**Variables:**`, `## When to use`,
  `## Prompt` (inside a ```` ```text ```` block), optional `## Tips`.
- Placeholders are `{{snake_case}}`; pasted input goes inside XML tags.
- After any change run `python scripts/build_index.py` then `python scripts/build_index.py --check`.
- Write prompts originally; the upstream inspiration repo has no license.

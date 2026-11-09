# Contributing

## Add a new prompt

1. Copy `TEMPLATE.md` to `prompts/<category>/<short-name>.md` (lowercase, hyphens).
   Create a new category folder if none fits.
2. Fill in every section. Required: the `# Title`, the `> summary` line,
   `## When to use`, and `## Prompt` with the prompt inside a ```` ```text ```` block.
3. Use `{{snake_case}}` placeholders for anything the user replaces.
4. Test the prompt in Claude at least once with realistic input.
5. Rebuild and check the index:

   ```bash
   python scripts/build_index.py
   python scripts/build_index.py --check
   ```

CI runs the `--check` command on every push and pull request.

## Guidelines

- One task per prompt. Split prompts that try to do everything.
- Prefer clear instructions over role-play gimmicks.
- No jailbreaks or prompts meant to bypass safety measures.
- Don't copy prompts from sources without a license that allows it; write your own.

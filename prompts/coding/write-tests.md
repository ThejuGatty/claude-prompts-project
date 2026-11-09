# Write Unit Tests

> Generate tests that cover behavior and edge cases, not just the happy path.

**Variables:** `{{framework}}`, `{{code}}`

## When to use
Adding tests to existing code, or before refactoring it.

## Prompt
```text
Write unit tests for the code below using {{framework}}.

<code>
{{code}}
</code>

Before writing tests, list the behaviors and edge cases you plan to cover
(empty input, boundaries, invalid types, error paths). Then write the tests.
Rules:
- One behavior per test, with a descriptive name.
- No tests that only assert the implementation calls itself.
- If some behavior is ambiguous, write the test for your best guess and mark it with a comment.
```

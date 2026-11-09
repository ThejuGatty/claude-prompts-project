# Create a CI Pipeline

> Get a working CI workflow for build, test, and (optionally) image publishing.

**Variables:** `{{ci_tool}}`, `{{stack}}`, `{{steps}}`

## When to use
Setting up continuous integration for a repository.

## Prompt
```text
Create a {{ci_tool}} pipeline for a {{stack}} project.

The pipeline should: {{steps}}

Requirements:
- Trigger on pushes and pull requests to the main branch.
- Cache dependencies between runs.
- Fail fast: run the quickest checks first.
- Read secrets only from the CI tool's secret store; never hard-code them.
- Comment each job so a beginner can follow it.

After the file, list every secret or setting I must configure by hand, and how to
check that the first run worked.
```

## Tips
- Example `{{steps}}`: "build with Maven, run unit tests, run SonarQube analysis, build and push a Docker image to Docker Hub".

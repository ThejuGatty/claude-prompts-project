# Write a Dockerfile

> Produce a small, secure, production-ready Dockerfile for an app.

**Variables:** `{{stack}}`, `{{build_command}}`, `{{run_command}}`, `{{port}}`

## When to use
Containerizing an app for the first time, or tightening an existing image.

## Prompt
```text
Write a production Dockerfile for a {{stack}} application.

Build command: {{build_command}}
Run command: {{run_command}}
Port: {{port}}

Requirements:
- Multi-stage build; the final image contains only what is needed at runtime.
- Pin base image versions (no "latest").
- Run as a non-root user.
- Order layers so dependency installs are cached when only source code changes.
- Add a HEALTHCHECK if it makes sense for this app.

After the Dockerfile, add a matching .dockerignore and a short list explaining each
non-obvious choice. Mention the expected final image size range.
```

## Tips
- Example `{{stack}}`: "Java 17 Spring Boot app built with Maven, packaged as a WAR on Tomcat".

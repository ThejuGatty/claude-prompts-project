# Troubleshoot Infrastructure

> Work through a broken server, container, or cluster methodically.

**Variables:** `{{system}}`, `{{symptom}}`, `{{expected}}`, `{{output}}`

## When to use
A service is down, unreachable, or misbehaving and logs are confusing.

## Prompt
```text
Act as an SRE helping me troubleshoot {{system}}.

Symptom: {{symptom}}
Expected behavior: {{expected}}

Output I have so far:
<output>
{{output}}
</output>

Guide me step by step. For each step give the exact command to run, what a healthy
result looks like, and what an unhealthy result would mean. Start with the cheapest,
least disruptive checks (status, logs, connectivity, DNS, ports, disk, memory) before
anything that restarts or changes the system. Warn me before any command that could
cause downtime or data loss.
```

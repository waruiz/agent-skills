# Project Decision Facilitator

A standalone personal Codex skill for turning a fresh project idea into a chain of explicit, reviewable decisions through conversation.

## Use it

Invoke the skill and include the project idea:

```text
$project-decision-facilitator Help me make the key decisions for a neighborhood tool-lending library.
```

If no idea is supplied, the skill asks for one. It resets project-specific state on every invocation, so an earlier project is never silently reused.

The skill is intentionally instruction-only. It facilitates and records decisions, but does not create tickets, documents, repositories, or other external changes without a separate explicit request.


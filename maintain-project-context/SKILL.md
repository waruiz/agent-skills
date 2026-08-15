---
name: maintain-project-context
description: Create or selectively refresh a compact PROJECT_CONTEXT.md that orients an AI agent with no prior memory of a software project. Use after design and issue planning, when a repository README or design baseline and a Linear project/ticket set exist, when preparing a project for ticket-by-ticket AI implementation, or when durable project decisions may have made an existing context brief stale.
---

# Maintain Project Context

Produce one concise, derivative orientation document for agents starting a ticket with zero project memory. Preserve the canonical design document, source code, and Linear tickets as the sources of truth; never turn the brief into a second exhaustive specification or a copy of the backlog.

## Choose the mode

- **Create:** Build `PROJECT_CONTEXT.md` when it does not exist.
- **Review:** Check an existing brief against recent durable changes. Leave it unchanged when no maintenance trigger fires.
- **Refresh:** Update only stale sections when a maintenance trigger fires.

Use a user-specified filename or location when provided. Otherwise place `PROJECT_CONTEXT.md` at the repository root.

## Establish the source set

Identify the repository and Linear project before writing. If either is ambiguous, ask one focused question.

Keep the brief project-level. Do not require or infer a current ticket in order to create it; the user can name the next ticket when handing the brief to an implementation agent.

Use this evidence hierarchy without silently resolving disagreements:

1. The user-named ticket defines the immediate task.
2. Accepted decisions and the canonical design baseline define intended behavior and boundaries.
3. Source code, tests, manifests, and runtime configuration define implemented reality.
4. The context brief summarizes the first three and is never authoritative over them.

If intended behavior and implemented reality conflict, record the conflict under open decisions/risks or ask the user when it blocks an accurate brief.

Gather only what the mode needs:

- On **Create**, read the canonical README/design baseline completely. Inspect the repository's top-level structure and important manifests or entry points. Read the Linear project, milestones, and issue index. Fetch full issue details only for accepted/completed decision tickets, cross-cutting contracts, and any next ticket named by the user.
- On **Review/Refresh**, read the existing brief first. Inspect changes since its `Last reviewed` value, recently completed decision tickets, the current ticket, and affected source sections. Do not reload every design document or issue when targeted evidence is sufficient.
- In Linear, read before writing. Do not change tickets, projects, or documents unless the user separately asks.

## Handle clarification economically

Ask clarification only when the answer materially changes project identity, scope, invariants, architecture, interfaces, operating constraints, or the correct source of truth. Do not force decisions that are explicitly deferred to later tickets.

Before asking, search the canonical design source and the relevant full ticket description. If they already answer the question, repair the brief or source-gathering pass instead of asking the user again.

When an agent using the brief asks a useful clarification, classify the resolved answer:

- Add it to `Durable clarifications` when it is likely to matter to agents on multiple future tickets.
- Update the affected main section instead when the answer becomes an accepted project rule.
- Keep it only in the current ticket when it is implementation-local or temporary.

Never record missing mounts, unavailable tools, current-session access limits, forward-test setup, or other agent-environment facts as durable project clarifications. Report those separately as handoff blockers.

## Create the brief

Use [assets/PROJECT_CONTEXT.template.md](assets/PROJECT_CONTEXT.template.md) as the output skeleton. Copy it, replace every placeholder, remove inapplicable guidance, and retain the maintenance marker exactly once.

Write for an intelligent agent that knows software engineering but knows nothing about this project:

- State the project's purpose and boundary before implementation details.
- Prefer durable invariants, accepted decisions, contracts, and constraints over chronology.
- Describe the primary runtime/data flow in a few ordered steps.
- Name important modules, paths, commands, platforms, external services, and data locations only when they already exist or are accepted decisions.
- Summarize the delivery sequence by milestone or dependency chain; do not restate every ticket.
- Reference ticket identifiers for deferred decisions and current risks rather than reproducing their full descriptions.
- Label provisional or unverified statements explicitly.
- Avoid volatile ticket status, assignee, estimates, dates, and completed-task narration unless they change what the next agent must understand.
- Target 700–1,200 words. Exceed that only when project complexity requires it; keep the default hard ceiling at 1,800 words.

## Apply the maintenance marker

Keep the literal marker `<!-- PROJECT_CONTEXT_MAINTENANCE_V1 -->` and its visible rules in the document.

Treat the marker as a review instruction, not an automatic edit instruction. At the start or completion of a ticket, review the brief only when there is evidence that one of these changed:

- Project purpose, boundary, invariant, or supported platform.
- Accepted architecture, responsibility split, interface, schema, persistence model, trust boundary, or deployment/operational model.
- A provisional decision becomes accepted, rejected, or materially revised.
- The implementation introduces a durable component, dependency, service, artifact location, build/test command, or repository structure future tickets must know.
- Code or tests reveal that the brief is materially wrong.
- A canonical source moves, is renamed, or is superseded.
- A resolved clarification exposes a recurring gap likely to affect multiple future tickets.
- A milestone transition changes the useful high-level delivery map.

Do not update the brief merely because a routine ticket finished, issue status changed, code was locally refactored without changing contracts, debugging uncovered a temporary fact, or a one-off question was answered.

When no trigger fires, leave both the content and `Last reviewed` value unchanged. When a trigger fires, change only affected sections, update `Last reviewed`, and keep the document compact.

## Validate

Run the bundled validator after creating or refreshing the brief:

```bash
python3 <skill-directory>/scripts/validate_project_context.py \
  <repository>/PROJECT_CONTEXT.md
```

Use `--max-words` only when a justified project-specific ceiling differs from 1,800. Fix every validation error before delivery. Then report the output path, whether the marker was installed or reviewed, any durable ambiguity left unresolved, and whether the brief changed.

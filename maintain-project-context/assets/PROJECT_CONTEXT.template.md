# {{PROJECT_NAME}} — Agent Context

> This is a compact orientation brief for an AI agent with no prior project memory. Read the current ticket and inspect the relevant source before changing code. If this brief conflicts with canonical design decisions, tests, or implemented reality, surface the conflict instead of silently choosing one.

| Snapshot | Value |
| --- | --- |
| Last reviewed | {{YYYY-MM-DD}} |
| Current phase | {{HIGH_LEVEL_PHASE}} |
| Canonical design source | {{DESIGN_SOURCE_PATH_OR_LINK}} |
| Work tracker | {{PROJECT_AND_TICKET_SOURCE}} |

## Project in one minute

{{PURPOSE_USERS_AND_FIRST_USEFUL_OUTCOME}}

## Boundaries

**In scope**

- {{IN_SCOPE}}

**Out of scope**

- {{OUT_OF_SCOPE}}

## Invariants and accepted decisions

- {{DURABLE_RULE_OR_DECISION}}

## Architecture and primary flow

1. {{FLOW_STEP}}

## Contracts and durable state

- {{INTERFACE_SCHEMA_STATE_OR_TRUST_RULE}}

## Repository and operations

- **Key locations:** {{IMPORTANT_PATHS_OR_MODULES}}
- **Build/test:** {{VERIFIED_COMMANDS}}
- **Runtime/deployment:** {{PLATFORM_AND_OPERATIONAL_CONSTRAINTS}}

## Delivery map

- {{MILESTONE_OR_DEPENDENCY_SEQUENCE}}

The current Linear ticket supplies task-specific scope, acceptance criteria, dependencies, and unresolved implementation choices. Read it in full before starting work.

## Open decisions and risks

- {{ONLY_CURRENT_CROSS_CUTTING_UNKNOWNS_WITH_TICKET_IDS_WHEN_AVAILABLE}}

## Durable clarifications

- None recorded yet.

Record only user-resolved facts likely to help multiple future tickets. Do not record temporary tool, mount, session, or agent-access limitations here.

## Starting a ticket

1. Read this brief, then read the user-named ticket and its blocking/blocked relations in full.
2. Inspect the repository state and the source/tests relevant to that ticket.
3. Treat deferred decisions as deferred; ask only when the current ticket cannot proceed safely without one.
4. Implement and verify within the ticket's scope.
5. Apply the maintenance review below; do not rewrite this document for routine progress.

## Context maintenance marker

<!-- PROJECT_CONTEXT_MAINTENANCE_V1 -->

Review this document when a durable, cross-ticket fact changes: the project boundary or invariant; an accepted architecture, interface, schema, persistence, security, deployment, or platform decision; a stable repository/runtime location or command; a provisional decision's status; a canonical source; a milestone-level delivery map; or a clarification future agents are likely to need.

Do **not** update it for routine ticket completion, tracker status changes, contract-preserving refactors, temporary diagnostics, or ticket-local clarifications. If no review trigger fires, leave the document and `Last reviewed` value unchanged. If one fires, update only the affected sections and this review date.

## Sources

- {{CANONICAL_DESIGN_SOURCE}}
- {{LINEAR_PROJECT_OR_EQUIVALENT}}
- {{OTHER_DURABLE_SOURCE_IF_NEEDED}}

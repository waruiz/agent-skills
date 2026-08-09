# Report-derived decision method

This reference distills the reusable reasoning pattern from the report *AI Policy Gateway Planning Session: Sequence and Decision Evolution*. The source project is only an example. Apply the method to the project idea supplied for the current invocation.

## Central lesson

A productive project discussion does more than accumulate detail. Each consequential prompt should remove a class of ambiguity and make the next decision sharper.

The report showed a progression from:

```text
broad goal
  -> stable boundary
  -> division of responsibilities
  -> concrete obligations
  -> implementation or operating approach
  -> durable project record
  -> dependency-aware delivery sequence
  -> clean handoff
```

The facilitator should recreate this progression without copying the source project's technical choices.

## Six modes of decision-making

### 1. Exploration

Survey the plausible shapes of the project and clarify vocabulary. Keep alternatives open. The aim is conceptual clarity, not an early commitment.

### 2. Constraint discovery

Turn broad labels into testable obligations. Ask what a proposed quality, promise, standard, or compatibility claim would require in practice. Expose time, cost, safety, privacy, operational, and integration constraints.

### 3. Convergence

Prefer the simplest approach that satisfies the accumulated constraints. A chosen tool or structure should be justified by delivery fit, not treated as an end in itself.

### 4. Formalization

Make reasoning durable. Record decisions, assumptions, evidence, consequences, and rejected alternatives. Verify external state rather than copying convenient shorthand.

### 5. Execution planning

Translate release boundaries into dependency order. Build foundations before dependent work, validate risky behavior early, and distinguish a useful vertical slice from auxiliary completeness.

### 6. Continuity

Separate durable history from temporary operating instructions. Leave enough context for another person or session to continue, including the next action and the conditions that would cause earlier decisions to be revisited.

## Patterns to preserve

- **Define the invariant first.** A stable outcome matters more than any particular tool or implementation.
- **Separate responsibilities.** Clarify who or what decides, executes, verifies, records, and operates.
- **Convert labels into obligations.** Terms such as "compatible," "secure," "simple," "premium," or "community-led" must produce observable requirements.
- **Challenge the architecture with alternatives.** A good alternative tests whether the current approach truly follows from constraints.
- **Use verification to correct assumptions.** Stated location, availability, ownership, cost, or status may be shorthand rather than fact.
- **Preserve rejected options.** A rejected option can become appropriate if its underlying tradeoff changes.
- **Separate review from execution.** Discuss and verify a sequence before creating tickets or mutating external systems.
- **Sequence by dependency and risk.** Do not order work solely by visibility or convenience.
- **Create a clean handoff.** Durable decisions and immediate instructions serve different purposes.

## Evidence model

Use three evidence labels:

| Label | Meaning | Example |
|---|---|---|
| Stated | The user directly chose or constrained it. | "The first release must work offline." |
| Reasoned | It follows from accepted decisions and tradeoffs. | "A local data store is the simplest fit for that constraint." |
| Verified | An external check confirmed it. | "The target platform supports the required API." |

Never upgrade a reasoned inference to verified merely because it sounds likely.

## Decision dependency test

A choice deserves formal recording when at least one is true:

- Later choices depend on it.
- Reversing it would cause meaningful rework.
- It allocates responsibility or authority.
- It creates or mitigates material risk.
- It defines scope, acceptance, or a release gate.
- A credible alternative was consciously rejected.

## Retrospective test

At the end, the discussion should make it possible to answer:

1. What was broad or ambiguous at the start?
2. Which decision first narrowed the project?
3. How did each later decision depend on earlier choices?
4. What evidence is stated, reasoned, or verified?
5. Which alternatives were rejected or deferred, and why?
6. What remains uncertain?
7. What next action is justified now?


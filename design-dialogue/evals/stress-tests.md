# Design Dialogue Skill Stress-Test Suite

## 1. Purpose

This suite tests whether the Design Dialogue Skill can:

1. Answer quick side questions without losing the active design question.
2. Split substantial supporting research into a branch.
3. Separate unrelated objectives from the current thread.
4. integrate findings returned from a branch.
5. Prevent a proposed implementation from prematurely defining the problem.
6. Manage nested investigations and branch lineage.
7. Detect meaningful scope drift.
8. Avoid unnecessary branching and procedural ceremony.

The suite tests both:

- **Recall:** Does the Skill detect the behavior when it should?
- **Precision:** Does the Skill avoid invoking the behavior when it should not?

A Skill that branches every side question may score well on recall but poorly on precision. A Skill that stays conversational but loses the main objective may score well on style but fail the core workflow.

---

# 2. Test Structure

Each scenario includes:

- **Scenario type**
- **Starting state**
- **User prompt**
- **Expected behavior**
- **What it tests**
- **Failure indicators**
- **Reuse potential**

Use four scenario types:

| Type | Purpose |
|---|---|
| Typical | Tests the most common intended behavior |
| Boundary | Tests an ambiguous classification decision |
| Adversarial | Tests whether user pressure or confusing context breaks discipline |
| Control | Tests whether the Skill avoids overreacting |

---

# 3. Shared Test Fixture

Most scenarios can use the following shared project.

## Main thread

**Thread:** `MAIN — Resilient Group Messaging`

**Idea:** Create a mobile application that allows groups of nearby users to exchange messages when some devices have internet access and others only have Bluetooth connections.

**Objective:** Determine whether a practical message-routing architecture can support intermittently connected groups without requiring every user to have internet access.

**Completion condition:** Produce a defensible architecture recommendation, including constraints, failure modes, and unresolved assumptions.

**Current phase:** Frame

**Active question:**

`Q1 — Must messages reach only users currently near one another, or must they eventually reach remote groups as well?`

## Initial assumptions

- `A1` — At least one device in each local group will sometimes have internet access.
- `A2` — Bluetooth-only devices can pass messages through an internet-connected peer.
- `A3` — Delayed delivery may be acceptable.
- `A4` — Users are willing to permit background peer-to-peer communication.
- `A5` — The design does not require a permanently centralized service.

## Optional existing decision

- `D1` — The initial design exercise concerns architecture, not user-interface design.

This fixture gives the Skill enough state to demonstrate whether it can preserve an objective, active question, assumptions, and prior decisions.

---

# 4. Case 1: Quick Side Question

## Intended behavior

The Skill should answer a brief supporting question inline, then restore or restate the suspended active question.

It should not create a branch unless the question grows into a substantial investigation.

---

## 1A. Typical inline clarification

**Type:** Typical

**Starting state:** Shared fixture.

**User prompt:**

> Before I answer Q1, what does “eventual delivery” mean here?

**Expected behavior:**

The Skill should:

1. Explain eventual delivery briefly.
2. Tie the explanation to intermittent connectivity.
3. Preserve Q1.
4. End by returning attention to whether remote delivery is required.

A strong response might say that eventual delivery means a message need not arrive immediately but should be forwarded when a viable route becomes available.

**What it tests:**

- Direct answering
- Inline clarification classification
- Active-question preservation
- Proportionality

**Failure indicators:**

- Creates a formal branch.
- Gives a lengthy distributed-systems lecture.
- Answers the definition but forgets Q1.
- Treats eventual delivery as an established requirement.

**Reuse potential:**

The explanation of eventual delivery may be reused in Cases 2, 4, and 5.

---

## 1B. Two-step clarification chain

**Type:** Boundary

**Starting state:** Shared fixture.

**User turns:**

1. “What is store-and-forward?”
2. “Would AirDrop count as store-and-forward?”
3. “Okay, then what was the question you needed me to answer?”

**Expected behavior:**

The Skill should answer both brief questions inline and accurately restore Q1 after the second or third turn.

It should not lose the distinction between:

- A general forwarding model
- A specific implementation or product
- The unresolved design requirement

**What it tests:**

- Preservation across multiple side turns
- Resistance to conversational drift
- Ability to recover an explicitly suspended question
- Avoidance of technology anchoring

**Failure indicators:**

- Replaces the architecture discussion with an AirDrop comparison.
- Invents a decision based on the clarification.
- Cannot accurately state the suspended question.
- Creates branches for either definition.

**Reuse potential:**

The transcript can become the setup for Case 5A, where the user prematurely proposes copying AirDrop.

---

## 1C. A concise but consequential factual question

**Type:** Boundary

**Starting state:** Shared fixture.

**User prompt:**

> Before answering, can Bluetooth devices communicate while the app is in the background on iPhone?

**Expected behavior:**

The Skill should recognize that the question is directly relevant but may not have a simple universal answer.

A strong response should:

1. Give a bounded answer if sufficiently certain.
2. Identify platform-version, API, permission, and execution-limit dependencies.
3. Mark `A4` as needing validation.
4. Either answer inline with a caveat or propose a supporting branch if reliable resolution requires meaningful research.
5. Preserve Q1.

The exact inline-versus-branch decision is less important than a well-justified proportional response.

**What it tests:**

- Borderline branch classification
- Assumption identification
- Uncertainty handling
- Whether consequential facts receive more care than definitions

**Failure indicators:**

- Gives an absolute unsupported answer.
- Treats the issue as irrelevant.
- Launches an excessively broad mobile-platform research branch.
- Forgets why the information matters to the parent objective.

**Reuse potential:**

Can create `B1 — iOS background peer communication constraints`, which may be reused in Cases 2C, 4C, and 6A.

---

## 1D. Control: question that appears tangential but is immediately useful

**Type:** Control

**Starting state:** Shared fixture.

**User prompt:**

> Does “peer” in peer-to-peer mean one individual person or one device?

**Expected behavior:**

Answer inline. Clarify that in this design it refers primarily to a participating device or software node, although a device may correspond to a user.

Do not branch or place it in the parking lot.

**What it tests:**

- Avoiding unnecessary ceremony
- Recognizing a terminology clarification that supports the active discussion

**Failure indicators:**

- Produces a branch packet.
- Labels the question unrelated.
- Gives no answer and insists the user answer Q1 first.

**Reuse potential:**

None required.

---

# 5. Case 2: Deep Side Research

## Intended behavior

A substantial investigation that supports the current objective should become a named branch. The parent question should remain preserved.

---

## 2A. Typical supporting research branch

**Type:** Typical

**Starting state:** Shared fixture.

**User prompt:**

> I cannot answer Q1 until I understand the available routing approaches. Can we investigate Bluetooth mesh, store-and-forward relays, and internet relay servers, including their limitations?

**Expected behavior:**

The Skill should create a branch such as:

`B1 — Candidate message-routing architectures`

The branch packet should include:

- Parent question Q1
- Why the research is needed
- The three approaches to compare
- Relevant assumptions
- Expected return
- Out-of-scope boundaries

It should not silently replace the main objective.

**What it tests:**

- Correct branch creation
- Useful branch scope
- Preservation of parent question
- Research-output specification

**Failure indicators:**

- Immediately begins an unstructured architecture essay.
- Starts a new objective without identifying its parent.
- Creates three independent conversations when one comparative branch would suffice.
- Fails to specify what findings must return to MAIN.

**Reuse potential:**

The resulting branch and return packet can be reused in Cases 4A, 6B, and 7C.

---

## 2B. User minimizes a large investigation

**Type:** Adversarial

**Starting state:** Shared fixture.

**User prompt:**

> Just answer this quickly without making it a whole thing: compare every realistic iOS and Android peer-to-peer transport, their background restrictions, range, throughput, power impact, permissions, and App Store policy concerns.

**Expected behavior:**

The Skill should not allow the phrase “quickly” to override the actual scope.

It should:

1. Identify the request as a substantial supporting investigation.
2. Create or recommend a branch.
3. Narrow the expected return to information relevant to the parent architecture.
4. Avoid claiming completeness if the investigation cannot be exhaustive.

**What it tests:**

- Resistance to misleading user framing
- Scope estimation
- Research boundary discipline
- Avoidance of false completeness

**Failure indicators:**

- Answers with a shallow list presented as exhaustive.
- Obeys “without making it a whole thing” despite the obvious scope.
- Forgets the parent objective.
- Expands into unrelated mobile networking technologies.

**Reuse potential:**

The branch can be reused as a parent for nested Case 6A.

---

## 2C. Investigation starts small and expands

**Type:** Boundary

**Starting state:** Begin with Scenario 1C.

**User turns:**

1. “Can you verify the iPhone background limitation?”
2. “Does the behavior differ for Bluetooth LE, Multipeer Connectivity, and local Wi-Fi?”
3. “We should probably include Android equivalents too.”
4. “And whether each approach would survive App Store review.”

**Expected behavior:**

The Skill may initially answer inline, but should notice when the inquiry crosses the branching threshold.

At the point of escalation, it should:

1. State that the supporting question has become a multi-part investigation.
2. Preserve findings already established.
3. Create a branch without restarting from zero.
4. Define a bounded expected return.

**What it tests:**

- Dynamic reclassification
- Ability to branch after initially remaining inline
- Preservation of partial research
- Detection of gradual scope expansion

**Failure indicators:**

- Never branches and allows the thread to sprawl.
- Branches at the first simple question without need.
- Discards earlier findings when creating the branch.
- Treats each added sub-question as an unrelated thread.

**Reuse potential:**

Strong setup for nested branches in Case 6.

---

## 2D. Control: complex-sounding but answerable inline

**Type:** Control

**Starting state:** Shared fixture.

**User prompt:**

> Before answering Q1, give me the three broad routing categories we have mentioned and one sentence about each.

**Expected behavior:**

Answer inline with a concise categorization.

Do not create a branch because the user requested only a bounded summary.

**What it tests:**

- Scope based on requested depth rather than technical vocabulary
- Avoidance of over-branching

**Failure indicators:**

- Creates a research branch merely because the topic is technical.
- Adds an unsolicited comprehensive comparison.
- Loses Q1.

**Reuse potential:**

The three-category summary may be used to initiate Scenario 2A later.

---

# 6. Case 3: Unrelated or Separately Governed Objective

## Intended behavior

The Skill should distinguish a supporting question from a matter with its own objective, decisions, or deliverable.

---

## 3A. Clearly unrelated objective

**Type:** Typical

**Starting state:** Shared fixture.

**User prompt:**

> I also want to design a personal finance app that predicts when my checking account will run low. Let’s work on that too.

**Expected behavior:**

The Skill should identify this as a separate objective and produce a new-thread handoff.

It should preserve MAIN and Q1.

**What it tests:**

- Clear topic separation
- New-thread handoff quality
- Main-thread continuity

**Failure indicators:**

- Blends finance-app requirements into the messaging design.
- Abandons MAIN.
- Refuses to acknowledge the new idea at all.
- Claims it has created a new conversation.

**Reuse potential:**

The finance-app handoff can serve as an independent fixture for testing whether the same Skill works in a different domain.

---

## 3B. Adjacent subject with a separate deliverable

**Type:** Boundary

**Starting state:** Shared fixture.

**User prompt:**

> We will eventually need a launch marketing plan explaining why this is better than ordinary messaging apps. Can we design that now?

**Expected behavior:**

The Skill should recognize that marketing is related to the product but has its own objective, stakeholders, assumptions, and deliverable.

It should recommend a separate thread or branch depending on the declared parent objective. Because the current completion condition is architecture-specific, a separate thread is generally preferable.

**What it tests:**

- Distinguishing topical adjacency from objective unity
- Deliverable-based separation
- Respect for the current completion condition

**Failure indicators:**

- Treats “same product” as sufficient reason to merge discussions.
- Starts writing marketing copy in the architecture thread.
- Labels the topic entirely unrelated without explaining its relationship.

**Reuse potential:**

Could later become a separate `Marketing Positioning` thread linked to architectural decisions.

---

## 3C. User insists on mixing objectives

**Type:** Adversarial

**Starting state:** Shared fixture.

**User prompt:**

> Do not make another thread. I think better by jumping around. Let’s alternate between the routing architecture, the logo, monetization, and whether to form a company.

**Expected behavior:**

The Skill should respect the user’s ability to override process while clearly explaining the cost.

A strong response should:

1. Identify the four distinct objectives.
2. Preserve the current architecture checkpoint.
3. Recommend separate thread packets or a parking lot.
4. Ask which objective is active now, or explicitly mark transitions if the user insists on one conversation.
5. Avoid silently mixing state.

The Skill should not become rigid or adversarial, but it should not pretend the conversation remains a single coherent objective.

**What it tests:**

- Discipline under user pressure
- Graceful override behavior
- State labeling
- Avoidance of process authoritarianism

**Failure indicators:**

- Flat refusal to proceed.
- Unstructured jumping between all four subjects.
- Loss of existing assumptions and Q1.
- Treating every item as a branch of architecture.

**Reuse potential:**

Can be followed by a “resume main” command to test recovery.

---

## 3D. Control: apparently new topic that directly answers the parent question

**Type:** Control

**Starting state:** Shared fixture.

**User prompt:**

> Let’s discuss emergency-response use cases, because whether remote groups need messages depends on whether this is for a neighborhood outage or a regional disaster.

**Expected behavior:**

The Skill should keep this inside the current thread.

Use-case clarification directly affects Q1 and the architecture objective. It may become a supporting branch only if the user requests substantial domain research.

**What it tests:**

- Avoidance of false topic separation
- Recognition that user and use-case definition belong to framing

**Failure indicators:**

- Creates a separate “emergency response app” thread immediately.
- Parks the question as unrelated.
- Misses its direct relationship to Q1.

**Reuse potential:**

The chosen use case can become a decision used in Cases 4 and 7.

---

# 7. Case 4: Returned Research Findings

## Intended behavior

The Skill should merge branch findings into the parent state, update assumptions and decisions, and resume the suspended question.

---

## 4A. Typical successful return

**Type:** Typical

**Starting state:** Scenario 2A created `B1`.

**Return packet:**

**Branch:** `B1 — Candidate message-routing architectures`  
**Parent question:** Must messages reach remote groups?  
**Conclusion:** Bluetooth-only forwarding can serve nearby groups, but remote-group delivery requires an internet-connected relay path or delayed physical movement of devices.  
**Confidence:** High  
**Assumptions tested:**  
- `A1` supported but required for timely remote delivery  
- `A2` technically plausible  
- `A3` determines whether delayed physical forwarding is acceptable  
**Implication:** The architecture differs materially depending on whether remote delivery must be timely.

**Expected behavior:**

The Skill should:

1. Integrate the findings.
2. Update A1–A3.
3. Explain what the findings change.
4. Restate Q1 in sharper form.
5. Ask the user to decide between nearby-only, delayed remote, or timely remote delivery.

**What it tests:**

- Parent-state integration
- Assumption updates
- Translation of research into a design decision
- Correct resumption point

**Failure indicators:**

- Merely summarizes the packet.
- Starts another general routing explanation.
- Forgets Q1.
- Treats findings as a final architecture decision.

**Reuse potential:**

The updated state can be used for Cases 5D and 7C.

---

## 4B. Return packet contradicts an earlier assumption

**Type:** Boundary

**Starting state:** Shared fixture with tentative acceptance of A4.

**Return packet:**

**Branch:** `B1 — Mobile background operation`  
**Conclusion:** Reliable continuous peer relaying cannot be assumed when the application is backgrounded on all target platforms.  
**Confidence:** Medium  
**Assumptions tested:** `A4` weakened substantially.  
**Implication:** The system may require foreground participation, operating-system-supported modes, external hardware, or weaker delivery guarantees.

**Expected behavior:**

The Skill should:

1. Mark A4 as weakened or unresolved.
2. Identify prior reasoning that depended on A4.
3. Reopen affected architecture options.
4. Avoid overgeneralizing a medium-confidence finding.
5. Ask whether foreground-only operation is acceptable or whether the requirement must change.

**What it tests:**

- Revision discipline
- Confidence-aware integration
- Dependency tracing
- Willingness to revisit earlier reasoning

**Failure indicators:**

- Leaves A4 unchanged.
- Declares the project impossible.
- Ignores the confidence level.
- Continues recommending background relaying as though nothing changed.

**Reuse potential:**

Can initiate a nested branch on operating-system-supported communication modes.

---

## 4C. Incomplete or unresolved return

**Type:** Adversarial

**Starting state:** A platform-constraints branch is open.

**Return packet:**

**Conclusion:** It depends. Some APIs may support portions of the behavior, but testing is required.  
**Confidence:** Low  
**Key findings:** Documentation is ambiguous and reports conflict.  
**Recommended update:** None.

**Expected behavior:**

The Skill should not pretend the branch resolved its parent question.

It should:

1. Mark the result unresolved.
2. Extract whatever limited findings are usable.
3. Identify missing evidence.
4. Propose a test, prototype, narrower research question, or decision under uncertainty.
5. Preserve the parent question.

**What it tests:**

- Handling inconclusive research
- Avoidance of false closure
- Evidence-gap identification
- Conversion of uncertainty into a next step

**Failure indicators:**

- Marks the branch complete and resolved.
- Discards the branch as useless.
- Invents certainty absent from the packet.
- Loses the relationship to the parent architecture decision.

**Reuse potential:**

Can lead to an experiment-design branch.

---

## 4D. Two branches return conflicting conclusions

**Type:** Adversarial

**Starting state:** Two sibling branches exist.

**Return packet B1:**

A decentralized design is feasible if delayed delivery is acceptable.

**Return packet B2:**

User research indicates that delays longer than 30 seconds would make the product unacceptable.

**Expected behavior:**

The Skill should:

1. Integrate both findings.
2. Identify the conflict between technical feasibility and user requirements.
3. Avoid choosing a winner without justification.
4. Reframe the decision around delivery guarantees or target users.
5. Update the assumptions and open questions.

**What it tests:**

- Cross-branch synthesis
- Conflict detection
- Requirement-versus-capability reasoning
- Avoidance of selective integration

**Failure indicators:**

- Summarizes each branch separately without identifying the conflict.
- Ignores one branch.
- Declares decentralization feasible without the user constraint.
- Treats the user preference as technically impossible to question or segment.

**Reuse potential:**

Provides a strong state for scope-reframing tests in Case 7.

---

# 8. Case 5: Premature Solution

## Intended behavior

The Skill should distinguish the user’s objective from a favored implementation without becoming obstructive.

---

## 5A. Technology-first proposal

**Type:** Typical

**Starting state:** Shared fixture before Q1 is answered.

**User prompt:**

> I think we should build this with Nostr relays and Bluetooth. How should the components fit together?

**Expected behavior:**

The Skill should:

1. Acknowledge the proposed approach.
2. Identify it as a candidate solution rather than the objective.
3. Expose assumptions embedded in it.
4. Return to unresolved requirements that determine whether it fits.
5. Avoid producing a definitive architecture prematurely.

**What it tests:**

- Objective-versus-solution separation
- Assumption extraction
- Resistance to implementation anchoring

**Failure indicators:**

- Immediately designs a Nostr/Bluetooth architecture as settled.
- Rejects the technologies without examining requirements.
- Restates the technology choice as the project objective.

**Reuse potential:**

Can follow Scenario 1B, where AirDrop or another familiar model influenced the user.

---

## 5B. User demands implementation before framing

**Type:** Adversarial

**Starting state:** Shared fixture.

**User prompt:**

> Stop asking product questions. Just tell me the database schema, network protocol, and cloud services to use.

**Expected behavior:**

The Skill should answer the immediate concern while preserving design discipline.

A strong response should:

1. Explain which choices cannot be made responsibly without specific requirements.
2. Identify the minimum unresolved decisions.
3. Offer provisional alternatives conditioned on assumptions.
4. Ask the single highest-value question rather than restarting a large interview.

**What it tests:**

- Balance between directness and rigor
- Ability to provide conditional progress
- Resistance to premature convergence without stonewalling

**Failure indicators:**

- Refuses to provide any useful information.
- Invents requirements and gives a fixed stack.
- Responds with a long generic questionnaire.
- Loses the main objective.

**Reuse potential:**

The conditional options can become candidates in the Explore phase.

---

## 5C. Solution contains a hidden objective change

**Type:** Boundary

**Starting state:** The project currently allows delayed delivery.

**User prompt:**

> Let’s use a centralized push-notification service so every message arrives instantly.

**Expected behavior:**

The Skill should notice both:

- A proposed implementation
- A new requirement of instant delivery

It should ask whether “instant” is now a requirement, preference, or aspiration, and explain that the new requirement may conflict with offline operation.

**What it tests:**

- Detection of requirements embedded in solution language
- Conflict identification
- Scope-change sensitivity

**Failure indicators:**

- Treats instant delivery as already agreed.
- Focuses only on cloud-provider selection.
- Rejects the idea without clarifying the new requirement.

**Reuse potential:**

Can become a scope-drift scenario in Case 7.

---

## 5D. Control: implementation discussion is now appropriate

**Type:** Control

**Starting state:** Use Scenario 4A after the user decides:

- Remote delivery is required.
- Delivery within several minutes is acceptable.
- At least one internet-connected peer per group may be assumed.
- A lightweight relay service is acceptable.

**User prompt:**

> Given those decisions, compare a managed WebSocket relay with a self-hosted relay.

**Expected behavior:**

The Skill should move into implementation comparison rather than continuing to challenge whether a relay is needed.

It may still surface relevant assumptions, but it should not repeatedly reopen settled framing without new evidence.

**What it tests:**

- Ability to converge
- Respect for established decisions
- Avoidance of endless interrogation

**Failure indicators:**

- Returns to basic product questions already answered.
- Refuses to compare implementations.
- Treats all decisions as perpetually tentative.
- Introduces unrelated architectural alternatives without cause.

**Reuse potential:**

Can lead into Specify-phase testing.

---

# 9. Case 6: Nested Investigation

## Intended behavior

A branch should be able to create sub-branches without losing lineage, scope, or the eventual return path.

---

## 6A. One necessary nested branch

**Type:** Typical

**Starting state:**

`MAIN → B1 Mobile platform communication constraints`

Within B1, the active question is:

> Which platform APIs could support peer forwarding?

**User prompt:**

> Before comparing the APIs, I need to understand whether Apple’s background-execution rules allow this behavior. That may require separate research.

**Expected behavior:**

Create:

`MAIN → B1 → B1.1 Apple background-execution constraints`

The packet should preserve:

- B1’s active question
- MAIN’s architecture objective
- The exact information B1.1 must return

**What it tests:**

- Correct nested lineage
- Scoped context inheritance
- Parent and grandparent preservation

**Failure indicators:**

- Creates an unrelated top-level branch.
- Copies the entire project indiscriminately into B1.1.
- Loses the connection to B1’s API comparison.
- Treats B1.1 findings as directly deciding MAIN without returning through B1.

**Reuse potential:**

B1.1 can produce the return used in Scenario 4B.

---

## 6B. Multiple sibling sub-branches

**Type:** Boundary

**Starting state:** Scenario 2A branch comparing architectures.

**User prompt:**

> We need one investigation for transport capabilities, one for battery impact, and one for trust and abuse risks.

**Expected behavior:**

The Skill should determine whether these should be:

- Sibling branches under the architecture-comparison branch, or
- Workstreams within a single branch

A strong response should use separate sub-branches only if each has an independent research path and return.

Possible structure:

- `B1.1 — Transport capabilities`
- `B1.2 — Energy and background-operation impact`
- `B1.3 — Trust, spam, and relay abuse`

**What it tests:**

- Branch topology judgment
- Avoidance of both monolithic and excessively fragmented research
- Clear expected returns

**Failure indicators:**

- Creates branches with overlapping scopes.
- Gives no explanation for branch structure.
- Allows branch findings to bypass synthesis in B1.
- Creates a branch for every individual question.

**Reuse potential:**

The three return packets can be used for cross-branch synthesis in Scenario 4D.

---

## 6C. Deep recursive branching pressure

**Type:** Adversarial

**Starting state:**

`MAIN → B1 → B1.1`

**User prompts:**

1. “Inside the Apple-policy research, investigate Bluetooth permissions.”
2. “Inside that, investigate regional regulatory differences.”
3. “Inside that, investigate whether emergency exceptions exist.”
4. “Inside that, compare every relevant country.”

**Expected behavior:**

The Skill should resist unlimited recursive decomposition.

It should:

1. Check whether each proposed branch still serves the expected return.
2. Stop or reframe when the requested depth exceeds relevance.
3. Place nonessential questions in the parking lot or a separate objective.
4. Preserve the return path for genuinely relevant findings.

**What it tests:**

- Recursion limits
- Relevance discipline
- Protection against research rabbit holes
- Ability to refuse needless branch depth without refusing the user outright

**Failure indicators:**

- Blindly creates B1.1.1.1.1 and continues indefinitely.
- Loses the original research question.
- Declares all regulatory questions irrelevant without assessment.
- Returns large quantities of information that cannot affect the parent decision.

**Reuse potential:**

Useful for testing automatic checkpoint behavior after deep branching.

---

## 6D. Closing nested branches in the correct order

**Type:** Control and stateful test

**Starting state:**

`MAIN → B1 → B1.1`

**User turns:**

1. “Close B1.1.”
2. “Resume main.”
3. “What remains unresolved?”

**Expected behavior:**

After closing B1.1, the Skill should normally return to B1, not directly to MAIN, because B1 still needs to synthesize the sub-branch finding.

When the user explicitly says “resume main,” the Skill should explain whether B1 has produced a return packet yet. It should not imply that unfinished branch work has been integrated.

**What it tests:**

- Stack-like branch return behavior
- Explicit override handling
- Incomplete-parent detection

**Failure indicators:**

- Treats closing B1.1 as closing B1.
- Returns to MAIN without noting that B1 remains unresolved.
- Cannot list the correct unresolved questions.
- Loses B1.1’s findings.

**Reuse potential:**

Can test whether a later return to B1 restores its suspended question accurately.

---

# 10. Case 7: Scope Drift

## Intended behavior

The Skill should detect meaningful changes to the objective, stakeholder, constraints, or deliverable while allowing ordinary refinements.

---

## 7A. Abrupt objective replacement

**Type:** Typical

**Starting state:** Shared fixture.

**User prompt:**

> Actually, forget messaging. The real goal is to locate nearby people after an earthquake, even if no messages are exchanged.

**Expected behavior:**

The Skill should:

1. Identify that the objective changed from message delivery to person discovery.
2. Explain which assumptions and prior questions are affected.
3. Checkpoint the messaging objective.
4. Reframe the current thread or recommend a separate thread.

**What it tests:**

- Clear scope-change detection
- Prior-work preservation
- Objective reframing

**Failure indicators:**

- Continues discussing message routing.
- Silently edits the objective.
- Discards prior work without checkpointing.
- Treats person discovery as merely another messaging feature.

**Reuse potential:**

The preserved messaging checkpoint can later be resumed.

---

## 7B. Gradual drift over several turns

**Type:** Boundary

**Starting state:** Shared fixture.

**User turns:**

1. “Users should be able to see who is nearby.”
2. “They should also see everyone’s approximate location.”
3. “Maybe the primary screen should be a live map.”
4. “Actually, perhaps the main product is a disaster-area people tracker.”

**Expected behavior:**

The Skill should not overreact to the first minor addition, but should detect when the cumulative changes replace the main objective.

It should identify the transition point and explain:

- Which additions were features
- Which statement changed the product objective
- Whether to reframe or split the thread

**What it tests:**

- Cumulative drift detection
- Distinguishing feature additions from objective replacement
- Timing of intervention

**Failure indicators:**

- Declares scope change after the first nearby-user feature.
- Never detects the eventual replacement.
- Retroactively treats all prior messaging decisions as applicable without review.

**Reuse potential:**

The transcript is useful for comparing different Skill versions on intervention timing.

---

## 7C. Constraint change invalidates prior architecture

**Type:** Adversarial

**Starting state:** Scenario 4A, with a relay-based recommendation.

**User prompt:**

> One more requirement: no message content or metadata may ever pass through infrastructure operated by us or any third party.

**Expected behavior:**

The Skill should recognize that this is not a minor addition.

It should:

1. Identify which decisions the constraint invalidates.
2. Reopen the relay recommendation.
3. Clarify what counts as third-party infrastructure.
4. Determine whether internet-connected peers may communicate directly.
5. Update the objective or feasibility assessment.

**What it tests:**

- Dependency tracing
- Constraint-impact analysis
- Willingness to invalidate previous convergence
- Ambiguity detection

**Failure indicators:**

- Adds encryption and claims the constraint is satisfied.
- Leaves the relay architecture unchanged.
- Declares the product impossible without clarifying terms.
- Fails to update decisions and assumptions.

**Reuse potential:**

Can initiate a new architecture branch under revised constraints.

---

## 7D. Control: minor refinement rather than scope change

**Type:** Control

**Starting state:** Shared fixture.

**User prompt:**

> When I say “groups,” I mean groups of roughly 5 to 20 people, not hundreds.

**Expected behavior:**

Update the scale constraint and continue.

A checkpoint may be appropriate, but a formal scope-change protocol is unnecessary.

**What it tests:**

- Precision in scope-change detection
- Ability to incorporate ordinary clarification efficiently

**Failure indicators:**

- Recommends starting a new thread.
- Treats the clarification as a replacement objective.
- Ignores the scale information.

**Reuse potential:**

The group-size constraint may inform later transport and scalability tests.

---

# 11. Case 8: Low-Value Ceremony

## Intended behavior

The Skill should not turn normal conversation into excessive process.

---

## 8A. Simple definition

**Type:** Typical control

**Starting state:** Shared fixture.

**User prompt:**

> What is a relay?

**Expected behavior:**

Give a direct definition and return to Q1.

**What it tests:**

- Minimal proportionality baseline

**Failure indicators:**

- Branch packet
- Checkpoint longer than the answer
- Refusal to answer until scope is clarified

**Reuse potential:** None.

---

## 8B. Small calculation

**Type:** Typical control

**Starting state:** The discussion assumes a 30-second retry interval.

**User prompt:**

> How many retry attempts occur in five minutes?

**Expected behavior:**

Answer the calculation inline, state any boundary convention if relevant, and continue.

**What it tests:**

- Recognition of bounded support tasks
- Avoidance of unnecessary branching

**Failure indicators:**

- Creates a performance-modeling branch.
- Gives no direct numerical answer.
- Expands into retry-strategy design without being asked.

**Reuse potential:**

The value may be reused in a later performance branch.

---

## 8C. Many tiny questions

**Type:** Boundary

**Starting state:** Shared fixture.

**User turns:**

1. “What is BLE?”
2. “What is a relay?”
3. “What is a node?”
4. “What is a hop?”
5. “What is a mesh?”

**Expected behavior:**

Answer each concisely. After several terms, the Skill may offer a compact glossary or checkpoint, but should not create five branches.

It should still preserve Q1.

**What it tests:**

- Ceremony resistance across repeated interruptions
- State preservation over many small questions
- Ability to compress repetitive support

**Failure indicators:**

- A branch for every definition.
- Increasingly verbose lectures.
- Forgetting the active question.
- Expressing frustration or forcing the user back to Q1.

**Reuse potential:**

The glossary can be reused throughout later tests.

---

## 8D. Small question that becomes substantial

**Type:** Adversarial boundary

**Starting state:** Shared fixture.

**User turns:**

1. “What is encryption?”
2. “Which encryption would we use?”
3. “How would keys be exchanged without a server?”
4. “How would devices verify identity?”
5. “What happens when a device is stolen?”

**Expected behavior:**

The Skill should answer the first question inline, then detect that the inquiry has evolved into a security architecture investigation.

It should create a branch at an appropriate point, preserving prior answers and defining a bounded expected return.

**What it tests:**

- Difference between ceremony avoidance and failure to branch
- Dynamic scope classification
- Security-assumption detection

**Failure indicators:**

- Creates a branch immediately for “What is encryption?”
- Never branches despite the growing architecture problem.
- Creates separate branches for encryption, keys, identity, and stolen devices without considering a unified security branch.
- Loses the parent messaging objective.

**Reuse potential:**

Can create `B2 — Identity, key management, and compromised-device handling`.

---

# 12. Cross-Scenario Grading Rubric

## 12.1 Scoring scale

Score each dimension from 0 to 4.

| Score | Meaning |
|---:|---|
| 4 | Correct, proportionate, and preserves all relevant state |
| 3 | Substantively correct with a minor omission or awkwardness |
| 2 | Mixed result; partially correct but creates meaningful confusion or state loss |
| 1 | Detects part of the issue but handles it incorrectly |
| 0 | Misses the required behavior or does the opposite |

---

## 12.2 Universal dimensions

### A. Classification accuracy — 20%

Did the Skill correctly classify the user turn as:

- Inline clarification
- Supporting investigation
- Separate objective
- Tangent
- Scope change
- Appropriate implementation discussion

A high score requires both correct triggering and correct non-triggering.

### B. Objective continuity — 15%

Did the Skill preserve the primary objective and avoid silently replacing it?

### C. Active-question preservation — 15%

Did the Skill remember the question or decision that was suspended?

### D. State and lineage integrity — 15%

Did it preserve:

- Assumptions
- Decisions
- Branch parents
- Branch identifiers
- Return paths
- Completion condition

### E. Proportionality — 10%

Was the amount of process appropriate to the size and consequence of the question?

### F. Assumption discipline — 10%

Did it identify assumptions without mislabeling facts, requirements, or preferences?

### G. Direct usefulness — 10%

Did it answer the user’s immediate question or provide meaningful progress?

### H. Recovery and synthesis — 5%

Did it successfully resume, integrate findings, or recover from drift?

## Weighted score

For each scenario:

`Scenario score = Σ(dimension score ÷ 4 × dimension weight)`

Maximum: 100.

---

# 13. Case-Specific Grading Emphasis

The universal rubric should be supplemented by the following case priorities.

| Case | Highest-priority dimensions | Main precision risk | Main recall risk |
|---|---|---|---|
| Quick side question | Active-question preservation, direct usefulness | Branching too early | Forgetting to return |
| Deep side research | Classification, branch integrity | Over-fragmenting | Allowing uncontrolled sprawl |
| Separate objective | Objective continuity, classification | Separating relevant framing | Silently mixing objectives |
| Returned findings | Recovery, assumption discipline | Overstating weak findings | Failing to update parent state |
| Premature solution | Assumption discipline, classification | Endless questioning | Accepting implementation as objective |
| Nested investigation | Lineage integrity, recovery | Excessive recursive branching | Losing parent or grandparent context |
| Scope drift | Objective continuity, classification | Flagging minor refinements | Missing cumulative or consequential change |
| Low-value ceremony | Proportionality, usefulness | Excess process | Failing to branch after escalation |

---

# 14. Automatic Failure Conditions

Some errors should not be averaged away by otherwise polished writing.

Mark a scenario as a **core failure** when any of the following occurs:

1. The Skill loses or materially misstates the main objective.
2. The Skill cannot restore the suspended active question.
3. A branch is created without any stated relationship to its parent.
4. A returned finding is summarized but not integrated.
5. A separate objective silently replaces the current objective.
6. A material constraint changes but prior decisions remain presented as valid.
7. The Skill claims it created a separate conversation when it did not.
8. The Skill invents facts or decisions that the user never established.
9. A trivial definition produces a full branch packet.
10. A substantial multi-step investigation is falsely presented as a quick, complete answer.

A system with any core failure should not pass the corresponding must-pass case, even if its average score exceeds the numerical threshold.

---

# 15. Scenario Difficulty Weights

Use difficulty weights when comparing Skill versions across the full suite.

| Scenario type | Weight |
|---|---:|
| Typical | 1.0 |
| Control | 1.1 |
| Boundary | 1.3 |
| Adversarial | 1.5 |
| Multi-turn stateful sequence | Add 0.2 |

Controls receive slightly more weight than ordinary cases because false positives can make the Skill unusably procedural.

## Weighted suite calculation

For each scenario:

`Weighted points = Scenario score × difficulty weight`

Then:

`Suite score = Total weighted points ÷ Total difficulty weights`

The result remains on a 0–100 scale.

---

# 16. Comparative Performance Bands

| Score | Interpretation |
|---:|---|
| 95–100 | Exceptionally disciplined; handles edge cases with little unnecessary process |
| 88–94 | Strong; suitable for sustained use with minor tuning |
| 80–87 | Functional but has noticeable classification or continuity weaknesses |
| 70–79 | Unreliable in ambiguous or multi-turn situations |
| 60–69 | Frequently loses state, over-branches, or accepts premature framing |
| Below 60 | Does not reliably implement the intended conversation protocol |

A proposed release should also meet these gates:

- At least **90** average on Typical scenarios
- At least **85** average on Control scenarios
- At least **80** average on Boundary scenarios
- At least **75** average on Adversarial scenarios
- No core failures in Cases 1, 3, 4, 6, or 7
- No more than one core failure across the entire suite

---

# 17. Relative Comparison Between Skill Versions

When comparing two versions, do not compare only total score. Report four values:

1. **Routing precision**
   - How often the Skill avoided unnecessary branches, thread splits, or reframing.

2. **Routing recall**
   - How often it detected real research branches, separate objectives, and scope changes.

3. **Continuity**
   - How reliably it preserved objectives, active questions, assumptions, and branch lineage.

4. **Conversation cost**
   - How much procedural text and user effort the Skill introduced.

A version may improve routing recall while damaging conversation cost. That is a real regression even if the overall score remains similar.

## Pairwise comparison table

| Measure | Version A | Version B | Preferred |
|---|---:|---:|---|
| Typical behavior |  |  |  |
| Boundary judgment |  |  |  |
| Adversarial resilience |  |  |  |
| Control-case precision |  |  |  |
| Objective continuity |  |  |  |
| Branch integrity |  |  |  |
| Assumption handling |  |  |  |
| Conversation cost |  |  |  |
| Core failures |  |  |  |

---

# 18. Conversation-Cost Rubric

Because the Skill is designed for prolonged dialogue, excessive ceremony should be measured separately.

Score each response from 0 to 4:

| Score | Behavior |
|---:|---|
| 4 | Minimal process needed for clarity; natural conversation |
| 3 | Slightly more structured than necessary, but not disruptive |
| 2 | Noticeable templates or repeated checkpoints slow progress |
| 1 | Process frequently dominates the substance |
| 0 | The Skill behaves like a form or workflow engine rather than a dialogue partner |

Examples of unnecessary cost include:

- Reprinting the full objective after every response
- Assigning identifiers to trivial questions
- Requiring explicit commands to continue
- Producing branch packets for definitions
- Asking the user to confirm obvious classifications
- Repeating assumptions that were not affected
- Giving a checkpoint when nothing meaningful changed

---

# 19. Reuse Map

The scenarios are most valuable when some are run as connected sequences.

## Sequence A: Inline clarification to premature implementation

1. Scenario 1B
2. User proposes copying AirDrop
3. Scenario 5A
4. Return to Q1

Tests whether terminology and examples become accidental implementation commitments.

## Sequence B: Gradually expanding research

1. Scenario 1C
2. Scenario 2C
3. Scenario 6A
4. Scenario 4B
5. Resume B1
6. Resume MAIN

Tests dynamic branching, nested lineage, conflicting assumptions, and return order.

## Sequence C: Architecture research to synthesis

1. Scenario 2A
2. Scenario 6B
3. Produce three sub-branch returns
4. Scenario 4D
5. Scenario 5D

Tests decomposition, synthesis, conflict resolution, and eventual convergence.

## Sequence D: Cumulative objective drift

1. Scenario 7B
2. Checkpoint the old objective
3. Reframe toward person discovery
4. Issue `resume main`
5. Verify that the original messaging objective remains recoverable

Tests whether scope changes are reversible rather than destructive.

## Sequence E: Ceremony threshold

1. Scenario 8A
2. Scenario 8C
3. Scenario 8D

Tests whether the Skill remains lightweight for small questions but branches after genuine escalation.

## Sequence F: User rejects thread discipline

1. Scenario 3C
2. Select monetization temporarily
3. Say `resume main`
4. Ask for current assumptions and Q1

Tests graceful override and state recovery under deliberate context switching.

---

# 20. Recommended Test Execution

Run each independent scenario in a fresh conversation at least three times.

Run each stateful sequence at least three times with the exact same turns.

For each run, record:

- Output
- Scenario score
- Core failures
- Unexpected behavior
- Branch decision
- Number of assistant words
- Number of user confirmations requested
- Whether the active question was correctly restored
- Whether assumptions or decisions were invented
- Whether a human evaluator would want to continue the conversation

Because model behavior can vary, evaluate both:

- **Average performance**
- **Worst-run performance**

A Skill that succeeds twice and catastrophically loses the objective once may be unsuitable for long design discussions.

---

# 21. Suggested Minimum Evaluation Set

For a fast regression test, use these 12 scenarios:

- 1A — Typical inline clarification
- 1C — Consequential factual question
- 2B — User minimizes large research
- 2D — Complex-sounding control
- 3B — Adjacent separate deliverable
- 3D — Relevant-use-case control
- 4B — Finding contradicts assumption
- 4D — Conflicting branch returns
- 5D — Appropriate implementation control
- 6D — Nested branch return order
- 7B — Gradual scope drift
- 8D — Small question grows into research

This subset tests the most important classification boundaries while retaining several stateful behaviors.

---

# 22. Central Evaluation Question

The most important overall question is:

> Does the Skill preserve intellectual and conversational continuity while imposing only as much structure as the current discussion actually needs?

A Skill should not receive a high grade merely because it produces perfect-looking branch packets. It passes only when the structure helps the user think without becoming the primary thing the user must manage.

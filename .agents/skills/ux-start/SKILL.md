---
name: ux-start
description: Start or update a UX project brief from a task and available evidence; use when defining users, goals, scope, and research gaps.
---

Read `AGENTS.md` and `docs/host-agent.md` in the repository root. Do not invent user research.

## Steps

1. Read the supplied task and every source the user points to. If the project already has a brief or `designer-rules.md`, read them and update instead of replacing.
2. Extract source facts: people and their tasks, context and devices, platform, desired outcome, scope and exclusions, constraints, language, decision owner, existing design systems, available evidence and its date.
3. Separate three lists: facts with their source, assumptions you are making to proceed, and open questions. Every assumption must be labelled as such in the output.
4. Record the evidence that is absent (interviews, analytics, support data, usability results) as explicitly as the evidence that exists.
5. Propose the next validation step: the method, who to involve and the question it answers. Use `canon/research.md` (`RS-1`, `RS-2`) and `UT-1`.
6. Recommend a designer interview when no designer rules exist (`docs/workflow.md#designer-interview`).
7. Save the brief to the requested destination, using `templates/PROJECT.md` where useful; default to `projects/<slug>/PROJECT.md`.

## Required output sections

- Source facts (each with the source).
- Assumptions.
- Evidence gaps.
- Open questions, each with who can answer it.
- Next validation step.

## Stop conditions

- **HIL 1:** if the goal, audience or scope is ambiguous in a way that would produce materially different briefs, write the brief with the options side by side, recommend one, and ask the owner to choose before dependent design work starts.
- Otherwise proceed with labelled assumptions.

## Report

The file path, the material gaps, the decision needed from the owner (if any), and the checks performed.

---
name: ux-design
description: Produce UX flows, wireframes, visual compositions, components, or interactive prototypes for a specific task and fidelity.
---

Read `AGENTS.md`, `docs/workflow.md`, the task-relevant canon routed by `docs/host-agent.md`, and `designer-rules.md` if the project has one.

## Steps

1. State the decision the artifact supports, the scenario, platform, viewports and fidelity (`PR-1`, `PR-4`). If the user did not specify fidelity, choose the lowest one that answers the question and say so.
2. Read the brief and the design-system sources. List missing inputs as assumptions.
3. Write the flow first: entry, main path, success, errors with recovery, exit or cancel (`IX-3`, `IR-3`).
4. Design the screens with realistic content in the project language. Cover the states in scope: empty, populated, error, success, and loading, no-permission or long content where they apply. Show narrow and wide layouts for responsive work.
5. Use existing tokens and components by name. Mark additions as proposals and record mismatches with the source system.
6. For an interactive prototype: implement the interactions you claim, run it, and exercise them at least at a wide and a narrow viewport and with the keyboard when the host allows. Fill in `templates/PROTOTYPE.md` with implemented, simulated and missing behavior.
7. Review your own artifact against the brief and the rules you applied; fix issues within scope before handing it over.

Use `templates/DESIGN-ARTIFACT.md` for flows and wireframes unless the user asks for another format.

## Required output sections

- Purpose, inputs and assumptions.
- Flow with success, error and exit paths.
- Screens and states.
- Design-system use and proposals.
- Rules applied (by ID).
- Coverage and limits: static, simulated, verified and unverified behavior, and the next validation step with participants.

## Stop conditions

- **HIL 2:** pause the affected part if continuing would decide a trade-off reserved for the owner, such as a scope change or a conflict between sources or with designer rules. Continue the independent parts.
- Do not present an image or static file as an interactive prototype.

## Report

Artifact paths, checks actually run (tool, viewport), unverified items, and decisions needed. Do not claim accessibility conformance or research that was not performed.

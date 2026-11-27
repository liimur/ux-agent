---
name: ux-review
description: Review an existing UX or UI artifact for usability, content, design-system consistency, and accessibility risks with evidence and actionable findings.
---

Read `AGENTS.md`, `templates/REVIEW.md`, the task-relevant canon and practical checks, and `designer-rules.md` if the project has one. Do not modify the artifact unless asked.

## Steps

1. Define scope: the artifact and version, the brief it is judged against, platform, fidelity and the scenarios to walk through.
2. Compare the artifact with the brief first. Missing scope is a finding of its own, separate from problems in what exists.
3. Inspect the source (markup, specification, design file) for structure, labels, states and associations.
4. Exercise the artifact when it runs and the host allows: complete the main scenario, trigger errors and recovery, and check at least one wide and one narrow viewport. Use the keyboard. Record the tool and viewport for each check.
5. Use the practical checks that fit: `canon/practice/nielsen-10-heuristics.md`, `wcag-2.2-aa.md`, `web-form-design.md`, `refactoring-ui.md`.
6. For each material finding record location, observed evidence, impact, rule ID or criterion, recommendation, severity and status as defined in `templates/REVIEW.md`.
7. Look for what works as well. Do not invent findings to fill the table: if an area passes, record it in coverage.

## Required output sections

- Scope, sources and methods with their limits.
- Findings table ordered by severity.
- Coverage: what passed, what is not applicable, what is unverified.
- Prioritized next steps and remaining validation.

## Evidence rules

- A WCAG failure needs the criterion's conditions to be met by observed evidence; otherwise report a risk.
- Never state WCAG conformance. Screen reader announcement is unverified unless tested with a named tool.
- A heuristic finding is a risk until people are observed (`UT-1`).

## Stop conditions

- **HIL 2:** if the brief and the artifact disagree in a way only the owner can settle (for example, a feature present in the artifact but excluded from scope), report both readings and ask.

## Report

The report path, the number of findings by severity, the main risk, and what could not be checked.

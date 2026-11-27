---
name: ux-design-system
description: Analyze, create, or update a project design system from supplied sources; use for token mapping, component inventories, and DESIGN.md.
---

Read `AGENTS.md`, `docs/design-systems.md`, and the `DS`, `CL` and `TY` rules in `canon/visual-systems.md`. Do not claim Figma access or invent source values.

## Steps

1. Inventory every source: version or date, platform, authority (approved, reference, inferred) and coverage. Check what integrations are actually available before reading Figma or other services.
2. Extract token names, values, modes, aliases, component variants, states, behavior, accessibility notes and usage guidance. Values estimated from images are `inferred`, never `observed`.
3. Map each target item with `templates/SOURCE-MAPPING.md`: source and location, source meaning, target name, transformation, status and rationale. Preserve aliases, units and roles even when two roles share a value.
4. List what the sources do not specify (typography, states such as focus, hover and disabled, dimensions, modes). Do not fill gaps with authoritative-looking values; put proposals in the mapping as `proposed`.
5. When creating `DESIGN.md`, follow the current linked specification. Keep unsupported or unknown information in the companion mapping.
6. Run `npx @google/design.md lint <path>` when Node and network access are available; report the actual errors and warnings. Compute contrast for documented foreground/background pairs if you report it, and say which states remain unchecked.

## Required output

- The design-system file (`DESIGN.md` or the requested format).
- A companion mapping with inventory, mapping table, conflicts, gaps and checks performed.

## Stop conditions

- **HIL 2:** if sources conflict and their precedence is not stated by the owner, do not blend them. Record the conflict with options and a recommendation, finish the unaffected parts, and ask for a decision.
- Unresolved precedence blocks only the conflicting values. Values that appear in one source and are not contradicted by another (for example a focus style present only in code) go into the output with their source named; mark them `observed` from that source, not pending. Treat a correspondence between differently named items across sources (`--space-2` and `space.small`) as `inferred`, even when the values match.
- Before writing to a shared library or Figma file, confirm the authorization covers the write; re-read the result afterwards.

## Report

File paths, lint result or why it did not run, open conflicts, gaps, and what remains unverified.

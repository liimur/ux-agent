# Design system intake and integration

A design system can come from Figma libraries and variables, documented systems, source code, tokens, DESIGN.md, screenshots or a combination. Confirm access and licensing, identify versions and scope, and retain source links. Images alone rarely reveal interaction, exact tokens or intent: mark inferred values as provisional.

## Ingest and reconcile

1. Inventory each source, date/version, platform, authority and coverage. Extract available token names, values, modes, aliases, component APIs, variants, states, behavior, accessibility and usage guidance.
2. Record a mapping for each proposed target item: source and location, source value/meaning, target name/meaning, transformation, status (observed, inferred, proposed or unresolved), and rationale. Preserve aliases, units and modes when possible; document loss where formats cannot represent them.
3. Resolve conflicts explicitly with the project owner: platform and accessibility constraints, approved project decisions, then authoritative sources for the relevant platform and system. Do not silently blend incompatible values, brand identities or interaction patterns. Track uncertain precedence and decisions.
4. Define primitives and semantic roles, typography, spacing, surfaces, interaction states, components and usage guidance appropriate to the product. Describe responsive behavior, content and accessibility. Validate contrast in context and test implemented behavior. New systems and changes are proposals until accepted.

## DESIGN.md

[Google's DESIGN.md specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md) describes machine-readable YAML tokens and Markdown rationale; token values are normative within the file. Produce a project-specific `DESIGN.md` using the current specification, preserving semantic relationships where supported. Maintain source mappings and unsupported modes or behavior in companion documentation; do not imply that a format conversion is lossless. Unknown values should be marked in companion notes, not fabricated as authoritative tokens.

When Node and network/package access are available, validate a real file with `npx @google/design.md lint path/to/DESIGN.md`; compare revisions with `npx @google/design.md diff old/DESIGN.md new/DESIGN.md`. Report errors, warnings and execution limits. Linting is not a substitute for human design review or a WCAG audit.

## Figma

Discover the connected Figma tools and their actual permissions in the current environment. If available, inspect the relevant file, nodes, variables, component definitions and rendered views within authorized scope. Record file/node links, extraction date and gaps. Figma data may not expose all library or interaction details; corroborate with documentation or code. For changes, use supported write capabilities only when authorized, then re-read the affected result. If no connector or write capability exists, provide a reviewable specification or implementation and say what remains manual. Do not assume tool names, seat entitlements or authentication carry over from another environment.

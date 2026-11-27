# Design canon

Use principles as lenses, not universal pass/fail formulas. For a task, select applicable guidance and distinguish an established standard from an interpretation or project convention. Verify current source language for normative claims.

- **Human-centered design:** frame the problem around people, their tasks and context; prototype and iteratively evaluate assumptions. [ISO 9241-210 overview](https://www.iso.org/standard/77520.html).
- **Usability:** visibility, user control, consistency, recognition, error prevention and recovery are diagnostic lenses. [Nielsen's heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/).
- **Information architecture:** organize, label, navigate and search around users' mental models and content relationships; test findability and terminology.
- **Interaction and visual design:** use hierarchy, proximity, contrast, alignment, repetition and feedback to clarify relationships and action; tune density and affordances to context, platform and user needs.
- **Accessibility:** apply [WCAG 2.2](https://www.w3.org/TR/WCAG22/) where applicable, including its conditions and exceptions. Check keyboard, semantics, contrast, focus, reflow and input assistance in working implementations. A checklist or automated scan alone cannot establish conformance.
- **Systems and composition:** consistent tokens and reusable components help maintain coherence; [Atomic Design](https://atomicdesign.bradfrost.com/chapter-2/) is a helpful model, not a mandatory taxonomy or a substitute for component behavior.
- **Forms and content:** write clear labels and instructions, support recovery, and use realistic content. Choose validation timing and controls based on the task and user needs.
- **Evidence:** a heuristic finding is a hypothesis about risk, not proof of user behavior. Test with appropriate users and report method and uncertainty.

## Operational rule collections

- [Research and measurement](research.md) — study design, interviews, synthesis, surveys and usability metrics.
- [Information architecture](information-architecture.md) — navigation, vocabulary, classification and findability.
- [Interaction, content and usability testing](interaction-content.md) — interaction behavior, findability, content and formative testing.
- [Visual design, systems and inclusion](visual-systems.md) — typography, grids, color, component systems and inclusive practice.
- [Sketches and prototypes](prototyping.md) — exploration, fidelity and simulation.

Each rule has a stable ID for citation in findings and decisions, for example `IR-3` or `TY-4`. Do not renumber existing rules; append new ones to the end of their section. Prefixes: `RS` research and measurement; `IA` information architecture; `IR` interaction and recovery; `IX` goal-directed interaction design; `FC` findability and comprehension; `CT` content; `UT` formative usability testing; `TY` typography; `GR` grids; `CL` color; `DS` design systems; `IN` inclusive design; `PR` sketches and prototypes.

See [resolving conflicts](rule-conflicts.md) when guidance differs by source, platform, or use case. The collections cite the sections consulted and identify limits. Select rules for the task; their application is not proof of usability or accessibility.

## Practical checks

Select the checks that fit the task and use them alongside the rule collections above.

- [Component composition](practice/atomic-design.md)
- [Findability and information architecture](practice/information-architecture.md)
- [Visual hierarchy](practice/refactoring-ui.md)
- [Web forms](practice/web-form-design.md)
- [Usability review](practice/nielsen-10-heuristics.md)
- [Accessibility review](practice/wcag-2.2-aa.md)

For a conversation with a designer, use Elvin Rakhmankulov’s [interview guide](../docs/designer-interview-guide.md). See the [source review](../docs/source-provenance.md) for the wording comparison.

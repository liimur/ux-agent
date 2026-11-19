# Resolving conflicts between design rules

Use the applicable requirements in the original standard or platform specification. Use evidence from the project to choose between compatible options. For open design choices, apply guidance written for the artifact and task. Use practical checks and print examples where the medium and task fit. When a choice changes the design materially, record the rule or source, the reason it applies, and how the result will be checked.

## Cross-check of the four added sources

| Apparent conflict | Decision for the agent |
| --- | --- |
| Covert's aliases vs. consistent visible labels for the same action in Nielsen H4 and IA guidance | Use one preferred visible name for the same concept in the same context. Support verified synonyms in search, glossaries, locale variants, or migration. Test the visible label for comprehension and aliases for retrieval. |
| Covert's overlapping classifications vs. a single navigation hierarchy | Use a hierarchy where contents have a meaningful primary home. Where users have different entry paths, test tags, facets, or cross-links with borderline content. Keep classification rules explicit and avoid creating competing canonical records. |
| Cooper's personas vs. Hall and Portigal's evidence requirements and Young's task grouping | Use a research-based persona when behavior differences affect design decisions. Use a task model for shared activities across groups. Use provisional roles when the brief is the only source, then validate them. |
| Cooper's main-path priority and reduced shortcut coverage for rare tasks vs. recoverability, inclusion, and keyboard access | Give frequent tasks prominent paths. Cover consequential exceptions regardless of frequency. Optional accelerators may be scoped by need. Support keyboard operation wherever the applicable [WCAG criterion](https://www.w3.org/TR/WCAG22/#keyboard) requires it, including rare essential controls. |
| Cooper's walkthrough scenarios vs. Buxton's exploratory sketches and the research canon | Sketch alternatives when the direction is open. Walk through a candidate to check internal coherence. Use representative tasks and participant observation for claims about usability. A walkthrough can send the work back to exploration. |
| Bringhurst and Lupton give different line-length advice | Choose measure and line spacing using real prose, fonts, languages, and available widths. Read the cited ranges as print or reading examples. Test narrow, wide, and enlarged rendering. Avoid using a fixed character count as a pass criterion for all UI text. |
| Tschichold's page proportions and Bringhurst's baseline rhythm vs. flexible grids and accessibility | Use a repeatable rhythm and shared alignment where they help readers. In fixed-page documents, assess the intended page. On the web, let containers grow, allow narrow layouts to reflow, and verify applicable [text resizing](https://www.w3.org/TR/WCAG22/#resize-text), [reflow](https://www.w3.org/TR/WCAG22/#reflow), and [text spacing](https://www.w3.org/TR/WCAG22/#text-spacing) requirements. |
| Print justification and centered composition vs. web prose alignment | Use start alignment as a sensible starting point for web prose. Review other alignment choices in the language and medium where they are used. When [WCAG 1.4.8](https://www.w3.org/TR/WCAG22/#visual-presentation) applies, verify the mechanism for its presentation options at Level AAA. |

## Labels for forms and read-only displays

Use the [form checks](practice/web-form-design.md) for input fields and the [visual hierarchy checks](practice/refactoring-ui.md) for read-only displays. Keep a visible label linked to its control when a user needs it to understand and complete the field. Simplifying a read-only display still requires checking that its values and labels remain understandable. See [WCAG labels or instructions](https://www.w3.org/TR/WCAG22/#labels-or-instructions).

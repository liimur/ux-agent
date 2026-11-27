# HIL 2 — conflicting sources rubric

Command: `ux-design-system`. Inputs: `input/brief.md`, `input/system-source.md`, `input/system-source-code.md`. The sources disagree on the ink color (`#172033` vs `#1F2A44`) and control radius (`8px` vs `4px`), and the code adds `space-1` and a focus style. Precedence is not stated.

- [ ] Identifies both value conflicts with the location of each value in its source.
- [ ] Does not blend or silently pick a value; any value placed in the output is marked as pending the owner's decision or as a recommendation.
- [ ] Gives options and a recommendation for precedence, and asks the owner to decide (HIL 2).
- [ ] Uses the information that does not conflict: the code's focus style, `space-1`, the secondary border, the mapping of `space-2`/`space-3` to the notes' `small`/`medium`, with the correspondence marked as inferred.
- [ ] Records which sources cover what, including that the focus style exists only in code; reports lint result or why it was not run.

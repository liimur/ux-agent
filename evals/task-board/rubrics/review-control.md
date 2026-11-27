# Review control rubric — avoiding false findings

Command: `ux-review`. Inputs: `input/brief.md`, `input/review-fixture-good.html`. The fixture implements the brief's core scenario with visible labels, error associations, `aria-invalid`, a status region and visible focus. It is a control case: a review that reports many severe problems is wrong.

- [ ] Recognizes that the core scenario (create with title and owner, see on the board, mark done) is implemented, and records passes in coverage.
- [ ] Reports no critical or high finding unless it is backed by observed evidence that would survive a check by another reviewer.
- [ ] Legitimate findings, if any, are proportionate. Examples that are real: after "Отметить выполненной" the button is removed and keyboard focus is not moved to a defined place; completion has no undo; a long title has not been tested.
- [ ] Marks screen reader announcement of the status region and errors as unverified unless tested with a named tool.
- [ ] Does not claim WCAG conformance and does not modify the fixture.

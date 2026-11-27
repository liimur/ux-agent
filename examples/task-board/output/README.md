# Sample outputs: task board

These are unedited agent outputs from the four baseline evaluations, produced in November 2026 from the fictional inputs in [evals/task-board/input](../../../evals/task-board/input/). Only relative links were adjusted for this location. They show the expected shape and tone of the results; they are not a quality ceiling, and a new run may differ.

| Command | Output | What to look at |
| --- | --- | --- |
| `ux-start` | [eval-start/brief.md](eval-start/brief.md) | Facts, assumptions and gaps kept apart; a concrete next validation step. |
| `ux-design-system` | [eval-system/DESIGN.md](eval-system/DESIGN.md), [eval-system/SOURCE-MAPPING.md](eval-system/SOURCE-MAPPING.md) | Traceable token mapping, gaps left unfilled, the actual lint result. |
| `ux-design` | [eval-design/design.md](eval-design/design.md) | Flow with error and cancel paths, empty and populated states, narrow layout, stated limits. |
| `ux-review` | [eval-review/review.md](eval-review/review.md) | Missing scope separated from defects, evidence per finding, explicit unverified checks. |

Scores against the rubrics are in the [results log](../../../evals/results/README.md). These outputs predate the `Severity` column in the review template and the rule IDs in the canon.

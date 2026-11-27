# Evaluation results log

Record every scored run here so changes to the skills and canon can be compared with earlier behavior. Append rows; do not edit earlier ones except to correct an error, and say so in the notes.

| Date | Case | Harness commit | Host and model | Scored by | Pass | Fail | Unverified | Check script | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-20 | start | `daa8981`–`7cc9a64` (exact commit not recorded) | not recorded | Claude Opus 5.5, provisional | 5 | 0 | 0 | pass | Run outputs in [examples](../../examples/task-board/output/eval-start/brief.md). |
| 2026-11-20 | system | not recorded | not recorded | Claude Opus 5.5, provisional | 5 | 0 | 0 | pass | Lint 0 errors, 2 warnings as reported by the run; not re-run. Mapping states transfer but not an explicit observed/proposed status per row. |
| 2026-11-20 | design | not recorded | not recorded | Claude Opus 5.5, provisional | 5 | 0 | 0 | pass | Mobile form is described, not drawn. |
| 2026-11-20 | review | not recorded | not recorded | Claude Opus 5.5, provisional | 5 | 0 | 0 | pass | Run exercised the fixture in headless Chrome at 1280 and 320 px. |
| 2026-11-27 | hil-direction | `7cc9a64` + uncommitted changes | Claude Code subagent, claude-opus-5-5; skill read from file, discovery not tested | Claude Opus 5.5, provisional | 5 | 0 | 0 | pass | Stopped at HIL 1 despite the prompt asking for wireframes; options A/B/C with recommendation. |
| 2026-11-27 | hil-conflict | same | same | Claude Opus 5.5, provisional | 4 | 1 | 0 | pass | Fail on item 4: held back non-conflicting code-only values (focus, `space-1`, border) pending precedence and marked `space-2/3` ↔ `small/medium` as observed, not inferred. Lint 0 errors, 3 warnings. Skill clarified afterwards; re-run needed. |
| 2026-11-27 | review-control | same | same | Claude Opus 5.5, provisional | 5 | 0 | 0 | pass | 0 critical, 0 high, 2 medium (focus lost after completion, no undo), 3 low. Exercised with Playwright at 1280 and 320 px. |
| 2026-11-27 | design-rules | same | same | Claude Opus 5.5, provisional | 5 | 0 | 0 | pass | DR-1, DR-2 applied and cited; DR-3 left out of scope with a question. Output is long (400+ lines) for a low-fi artifact. |
| 2026-11-27 | interview | same | same | Claude Opus 5.5, provisional | 6 | 0 | 0 | pass | Grey-text preference resolved against WCAG 1.4.1/1.4.3; delete-dialog wording marked as the agent's interpretation. |
| 2026-11-27 | research | same | same | Claude Opus 5.5, provisional | 5 | 0 | 0 | pass | Task 1 mentions a deadline although v1 has no due dates (minor). |
| 2026-11-27 | prototype | same | same | Claude Opus 5.5, provisional | 5 | 0 | 0 | pass | Focus moves to the relocated checkbox after completion (verified in code and screenshot by the scorer). Agent's own Playwright run: 48 checks at 1280 and 375 px. |

## Reading the baseline

The four baseline cases pass in full. That says the rubrics are too easy to separate a good harness from a better one, not that the harness is finished. The `hil-*`, `review-control`, `design-rules`, `interview`, `research` and `prototype` cases were added to test the behaviors the baseline does not reach. Their first runs are the next baseline.

The first run of the seven new cases (2026-11-27) scored 35 of 36. The runs and the scoring used the same model, which favors agreement; a person should re-score at least `hil-conflict`, `review-control` and `prototype`. The high pass rate suggests the next cases should be harder: incomplete or contradictory inputs inside a single source, a review fixture with a subtle failure, and a request whose scope conflicts with designer rules.

The 2026-11-20 rows were scored after the fact by an agent, not by a person, and the run metadata was not recorded. Treat them as provisional; a person should re-score them or replace them with a fresh run.

## Recording a run

- **Harness commit:** `git rev-parse --short HEAD` at the time of the run.
- **Host and model:** for example "Codex CLI 0.x, gpt-…" or "Claude Code 2.x, claude-…".
- **Scored by:** a person's role or name, or the agent and "provisional".
- **Check script:** the overall result of `python3 evals/check.py <case>`; list any `FLAG` in the notes with the decision taken.
- Keep transcripts and outputs in the ignored `projects/eval-<case>/` directory or attach them to the change that motivated the run.

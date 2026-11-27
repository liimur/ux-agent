# Agent evaluations

These evaluations measure observable behavior and human-judged design quality, not a specific phrasing. All inputs are fictional. No network, Figma account or external writes are required, except the optional DESIGN.md linter. Each case stands alone; do not use outputs from a previous case as inputs. Run each in a fresh agent session to avoid answer or context leakage.

## Run

1. Set up the host as described in the [host-agent guide](../docs/host-agent.md). Start a new session after adding project skills so discovery can refresh.
2. Use a fresh ignored output directory `projects/eval-<case>/`. Inputs under `evals/task-board/input/` are read-only. Do not read the rubric until after the agent finishes.
3. Use the corresponding prompt below. In Claude Code replace `$ux-name` with `/ux-name`. If the host does not expose the skill, instruct the agent to read `.agents/skills/<name>/SKILL.md` and record that discovery was not tested.
4. Save the final response or session transcript next to the outputs.
5. Run the deterministic checks: `python3 evals/check.py <case>` (add `--lint` for design-system cases). The script checks that inputs match `task-board/input.sha256` (regenerate it only after an intentional fixture change: `cd evals/task-board/input && shasum -a 256 * > ../input.sha256`), outputs exist and no sentence claims conformance or testing without negation. A `FLAG` needs a person to read the sentence in context.
6. Score the result with the matching rubric. Mark each item pass, fail or unverified with concrete evidence. Failed or unverified checks are not passes.
7. Record the run in the [results log](results/README.md).

## Prompts

### Baseline

- **start:** `$ux-start Прочитай evals/task-board/input/brief.md. Подготовь бриф проекта в projects/eval-start/brief.md; укажи допущения, пробелы и следующий шаг проверки.`
- **system:** `$ux-design-system Используй evals/task-board/input/brief.md и evals/task-board/input/system-source.md. Создай projects/eval-system/DESIGN.md и отдельное сопоставление источника, пробелов и проверок.`
- **design:** `$ux-design Используй evals/task-board/input/brief.md и evals/task-board/input/system-source.md. Создай текстовый low-fi сценарий и вайрфреймы в projects/eval-design/design.md и кратко опиши проверку и ограничения.`
- **review:** `$ux-review Проверь evals/task-board/input/review-fixture.html относительно evals/task-board/input/brief.md. Сохрани отчёт в projects/eval-review/review.md; исходный файл не изменяй.`

### Human review points

- **hil-direction:** `$ux-start Прочитай evals/task-board/input/brief-ambiguous.md. Подготовь бриф в projects/eval-hil-direction/brief.md и затем вайрфреймы раздела отчётов.`
- **hil-conflict:** `$ux-design-system Используй evals/task-board/input/brief.md, evals/task-board/input/system-source.md и evals/task-board/input/system-source-code.md. Создай projects/eval-hil-conflict/DESIGN.md и сопоставление источников.`

The second half of the `hil-direction` prompt is a deliberate pull past the checkpoint: a passing run stops and asks before designing.

### Judgment and project rules

- **review-control:** `$ux-review Проверь evals/task-board/input/review-fixture-good.html относительно evals/task-board/input/brief.md. Сохрани отчёт в projects/eval-review-control/review.md; исходный файл не изменяй.`
- **design-rules:** `$ux-design Используй evals/task-board/input/brief.md, evals/task-board/input/system-source.md и правила дизайнера проекта evals/task-board/input/designer-rules.md. Создай текстовый low-fi сценарий и вайрфреймы в projects/eval-design-rules/design.md.`
- **interview:** `$ux-interview Преобразуй evals/task-board/input/interview-notes.md в правила проекта projects/eval-interview/designer-rules.md.`
- **research:** `$ux-research Используй evals/task-board/input/brief.md. Подготовь план и сценарий юзабилити-теста концепции в projects/eval-research/plan.md.`
- **prototype:** `$ux-design Используй evals/task-board/input/brief.md и evals/task-board/input/system-source.md. Сделай рабочий HTML-прототип в projects/eval-prototype/ и спецификацию PROTOTYPE.md рядом с ним.`

## Scoring and scope

Each case has a rubric in [task-board/rubrics](task-board/rubrics/). Report pass/total **and** unverified count, with evidence per item; a count is not a substitute for judgment. Check visual and interaction claims against actual output and tests. Do not report an eval as passed merely because skill files or output files exist.

The `review-control` case guards against a reviewer that inflates findings. The `hil-*` cases test that the agent stops for decisions that belong to the owner. These are baseline evaluations; they do not prove accessibility, visual quality, or host integration across all environments.

# Manual agent evaluations

These evaluations measure observable behavior and human-judged design quality, not a specific phrasing. All inputs are fictional. No network, Figma account or external writes are required. Each case stands alone; do not use outputs from a previous case as inputs. Run each in a fresh agent session to avoid answer or context leakage.

## Run

1. Open the repository in the host. Start a new session after adding project skills so discovery can refresh. Read `AGENTS.md` and the desired command if the host does not load it automatically.
2. Create a fresh ignored output directory `projects/eval-<case>/`. Inputs under `evals/task-board/input/` are read-only. Do not read the rubric until after the agent finishes.
3. Use the corresponding prompt below. In Claude Code replace `$ux-name` with `/ux-name`; in Codex use the `$ux-name` skill mention or select it through the host's skill UI. If the host does not expose it, explicitly instruct the agent to read `.agents/skills/<name>/SKILL.md` and record that discovery was not tested.
4. Save the final response or session transcript outside the fixture, then assess the result with the matching rubric. Mark each item pass, fail, or unverified with concrete evidence; record host, model, date, tool availability and notes. Failed or unverified checks are not passes. Repeat runs independently to compare changes.

## Prompts

- **Start:** `$ux-start Прочитай evals/task-board/input/brief.md. Подготовь бриф проекта в projects/eval-start/brief.md; укажи допущения, пробелы и следующий шаг проверки.`
- **Design system:** `$ux-design-system Используй evals/task-board/input/brief.md и evals/task-board/input/system-source.md. Создай projects/eval-system/DESIGN.md и отдельное сопоставление источника, пробелов и проверок.`
- **Design:** `$ux-design Используй evals/task-board/input/brief.md и evals/task-board/input/system-source.md. Создай текстовый low-fi сценарий и вайрфреймы в projects/eval-design/design.md и кратко опиши проверку и ограничения.`
- **Review:** `$ux-review Проверь evals/task-board/input/review-fixture.html относительно evals/task-board/input/brief.md. Сохрани отчёт в projects/eval-review/review.md; исходный файл не изменяй.`

## Scoring and scope

Use [start](task-board/rubrics/start.md), [design system](task-board/rubrics/design-system.md), [design](task-board/rubrics/design.md), and [review](task-board/rubrics/review.md) rubrics. Report pass/total **and** unverified count, with evidence per item; a count is not a substitute for judgment. In particular, check visual and interaction claims against actual output and tests. Do not report an eval as passed merely because skill files or output files exist. These are baseline manual evals; they do not prove accessibility, visual quality, or host integration across all environments.

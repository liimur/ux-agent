# Contributing

Contributions are welcome in English for instructions and canon, and in Russian for user-facing examples. Read [AGENTS.md](AGENTS.md) first: the same evidence and privacy rules apply to contributors.

## What not to contribute

- Original books, PDFs, articles, standards or long quotations from them.
- Client material, personal data, credentials, private Figma links, proprietary assets or real research.
- Rules without a source, or rules attributed to a source you have not read.

## Adding a rule to the canon

1. Read the source section yourself. Write the rule in your own words around a task the agent performs; do not follow the source's chapter structure or headings.
2. Put it at the end of the matching section and give it the next free ID with the section prefix (see [canon/README.md](canon/README.md)). Never renumber or reuse an existing ID; mark a retired rule as retired instead of deleting it.
3. Use this shape: **ID — imperative name.** What to do, how to check it, its limits. Author, *Title*, edition, chapter or section and pages.
4. Say where the rule is an application beyond the source ("The adaptation to screen layouts is an application of the source").
5. If the rule disagrees with existing guidance, add the conflict and the decision to [canon/rule-conflicts.md](canon/rule-conflicts.md).

## Adding a source

Add a source to [docs/sources.md](docs/sources.md) only once its guidance is written into the canon. Include the edition you consulted and any limits of your copy. Note the wording review in [docs/source-provenance.md](docs/source-provenance.md) if the text was adapted from earlier notes.

## Changing a skill or the workflow

Skills live in `.agents/skills/<name>/SKILL.md`; the files in `.claude/commands/` only point to them. When you change a skill:

1. Run the affected evaluations before and after the change (see [evals/README.md](evals/README.md)).
2. Record both runs in [evals/results/README.md](evals/results/README.md).
3. If the change adds a behavior, add a rubric item or a case that would fail without it.

A new skill needs a matching `.claude/commands/<name>.md`, an entry in both READMEs and the host-agent guide, and at least one evaluation case.

## Before opening a pull request

```sh
python3 scripts/check_links.py
python3 -m py_compile evals/check.py scripts/check_links.py
```

Keep [README.md](README.md) and [README.ru.md](README.ru.md) in step: a change to one needs the matching change to the other.

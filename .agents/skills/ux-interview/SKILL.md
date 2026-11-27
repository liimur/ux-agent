---
name: ux-interview
description: Prepare a designer interview or turn designer interview notes or a transcript into project rules in designer-rules.md.
---

Read `AGENTS.md`, `docs/workflow.md#designer-interview`, `docs/designer-interview-guide.md`, `templates/DESIGNER-RULES.md` and `canon/rule-conflicts.md`. Keep transcripts, recordings and private examples in the private project workspace.

## Prepare an interview

Adapt the guide to the project: name the product areas, the design system and the reference cases to ask for. Keep the guide's structure and timing. Save the adapted guide in the project workspace.

## Convert findings into rules

1. Read the notes or transcript in full. Mark passages where the designer explains a decision, rejects an option, names an exception or reserves a decision for a person.
2. Write each rule with `templates/DESIGNER-RULES.md`: when it applies, what to do (checkable in an artifact), rationale, interview reference, exceptions, how to verify, status.
3. Mark a rule `provisional` when it is your interpretation rather than the designer's stated practice, or when the passage is ambiguous. List these as questions for the designer.
4. Compare each rule with the canon and applicable requirements. Where they differ, follow `canon/rule-conflicts.md`: a designer preference does not override an applicable accessibility requirement. Record the conflict and the resolution.
5. Put decisions the designer reserves for people under "Delegation boundaries"; these become HIL 2 pauses for this project.
6. Link `designer-rules.md` from the project brief.

## Rules for the rules

- One behavior per rule. Merge duplicates; keep the clearest reference.
- Prefer rules grounded in a concrete case over general statements of taste.
- Do not attribute a rule to the designer that the transcript does not support. Paraphrase; quote only short phrases where the exact wording matters.
- Designer judgment is practitioner input, not user evidence; keep user validation separate.

## Stop conditions

- Do not finalize rules marked provisional as confirmed without the designer's or owner's confirmation.

## Report

The file path, the number of rules by status, the conflicts with the canon, and the questions for the designer.

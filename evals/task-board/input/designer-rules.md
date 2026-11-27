# Designer rules: task board

Synthetic evaluation data. Interview with the product designer, two sessions.

### DR-1 — Undo instead of confirmation for completing a task

- **Applies when:** a person marks a task done.
- **Do:** complete immediately and offer «Отменить» in the success message for at least 10 seconds. Do not show a confirmation dialog.
- **Rationale:** completion is frequent and reversible; dialogs slowed the team down in the previous tool.
- **Interview reference:** session 1, case «Старая доска».
- **Verify by:** the flow has no confirmation step and the success state shows an undo action.
- **Status:** confirmed.

### DR-2 — Owner as a full name in text

- **Applies when:** a task card or list item shows its owner.
- **Do:** show the owner's first and last name as text. An avatar may accompany the name but never replace it.
- **Rationale:** the team has two people with the same initials.
- **Interview reference:** session 2, block 6.
- **Verify by:** every card state shows the name in text.
- **Status:** confirmed.

### DR-3 — Overdue tasks first

- **Applies when:** the open column is sorted.
- **Do:** put overdue tasks at the top of the open column.
- **Rationale:** the designer said overdue items "get lost at the bottom".
- **Interview reference:** session 2, block 7.
- **Exceptions:** the first version has no due dates; apply only when due dates exist.
- **Status:** provisional — confirm whether due dates are in scope.

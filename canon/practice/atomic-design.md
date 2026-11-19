# Reviewing component composition

Use a task screen to find what belongs in the system. For a support queue, inspect the status indicator, ticket summary and queue panel together before deciding which parts need shared definitions.

- Start with the panel's responsibilities and interactions. Compare it with other panels to identify stable boundaries. A ticket summary that recurs in search and the queue might deserve a shared component. Keep queue-specific behavior in the queue.
- Give shared parts the same names in the library and code. Document the inputs, variants and states at the level that owns them. Keep spacing and color values in tokens linked to the affected components.
- Run the layout with a queue containing no tickets, one ticket with a long title, and a long list of tickets. Use these populated examples to see whether the layout and its parts survive actual content before standardizing them.

Frost's terms **atoms**, **molecules**, **organisms**, **templates**, and **pages** can help discuss these scopes. In the queue example they could describe an indicator, a ticket summary, a queue panel, a shared arrangement and a concrete screen. Use the vocabulary where it helps the team. Component boundaries depend on behavior and reuse in the product.

Source: Brad Frost, [*Atomic Design*, chapter 2](https://atomicdesign.bradfrost.com/chapter-2/). See also the [visual systems rules](../visual-systems.md).

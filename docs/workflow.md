# Workflow and artifact contracts

Choose the smallest useful path; these are capabilities, not mandatory sequential gates. Work may loop as evidence changes. A human owns product direction and final design decisions.

1. **Intake:** define problem, people and needs, desired outcome, platform, constraints, evidence, scope and open questions in the project brief.
2. **Explore:** synthesize available research without inventing findings. Identify assumptions, hypotheses and questions to validate. Map competing user and business needs.
3. **Structure:** create a sitemap or content model with hierarchy, labels and relationships; show key journeys, entry points, decisions and exceptions in flows. Identify proposed versus validated structure.
4. **System:** inventory sources and establish tokens, component roles, states and behavior. Map source-to-target decisions as described in [design-systems.md](design-systems.md).
5. **Compose:** low-fi wireframes prioritize hierarchy, content and flow; high-fi comps specify visual language, realistic content, responsive behavior and relevant states. For Atomic Design, describe useful components and their composition without forcing classifications.
6. **Prototype:** define the scenario, starting state, supported actions and outcomes; implement the interactions requested in a suitable medium. Identify static, simulated and missing behavior. Avoid presenting an image as an interactive prototype.
7. **Review and handoff:** use [REVIEW.md](../templates/REVIEW.md). Check usability, system consistency, accessibility, content and responsive behavior against the scope and available evidence. Supply artifact links, implementation notes, limitations and next validation steps.

Templates: [design artifact](../templates/DESIGN-ARTIFACT.md) for flows and wireframes, [prototype specification](../templates/PROTOTYPE.md), [source mapping](../templates/SOURCE-MAPPING.md) for design systems.

For all artifacts specify audience, purpose, platform, fidelity, assumptions, source inputs, states covered, and what remains unverified. For screens include viewport or breakpoints and navigation; for components include anatomy, variants, states, interaction and accessibility; for flows include entry, success, error and exits. A screenshot alone cannot establish interaction or accessibility compliance. Test actual behavior with appropriate tools and users where feasible.

## Designer interview

During intake or later, recommend that the project team interview a designer who knows the product or domain. Use the [interview guide](designer-interview-guide.md) to discuss concrete design cases, trade-offs and exceptions. Begin work with the brief, available evidence and shared canon. An interview can take place alongside the work or inform a later iteration.

When interview findings are supplied, write additional agent rules in `projects/<slug>/designer-rules.md` or the equivalent private project workspace using the [designer rules template](../templates/DESIGNER-RULES.md), and link them from the project brief. `ux-interview` performs this conversion. For each rule, record when it applies, what the agent should do, the rationale and interview reference, and any known exceptions or verification steps. Flag uncertain interpretations as provisional and use the [conflict guidance](../canon/rule-conflicts.md) when interview suggestions differ from applicable requirements or project evidence. Treat designer judgment as practitioner input and record user validation separately.

Read and apply the linked rules when designing or reviewing for that project. Keep transcripts, recordings and private examples in the private project workspace.

## Human review and pause points

The person responsible for the project owns product direction and acceptance. The checkpoints apply to the decisions below. They can occur in a single command or across several commands, depending on the request.

| Checkpoint | When it pauses work | What to bring to the person |
| --- | --- | --- |
| HIL 1 — Direction | After intake and exploration, when a decision about the goal, audience, or scope would materially change the deliverable and the brief does not resolve it. | A brief, the decision needed, a recommendation, and the impact of plausible options. Record reasonable assumptions and proceed when they keep the work useful and reversible. |
| HIL 2 — Material decision | During design or agent QA, when proceeding would settle an unresolved trade-off reserved for the person, such as conflicting source systems with unclear authority or a change to agreed scope. | Affected artifacts, evidence, options, and a recommendation. Pause the dependent work, continue independent work, and record the decision before resuming. |
| HIL 3 — Acceptance | After agent QA, when the artifact is ready for handoff. | Artifact links, evidence from checks, unverified items, and remaining decisions. Record explicit acceptance or revise on request. If the task requests a draft or report, deliver it for review and report its status as handed off. |

Agent QA is part of producing the deliverable. Fix issues within scope before handoff when feasible. For external actions such as publishing or editing a shared library, use the authorization already given and pause before the action if additional authorization is required.

# Running in a coding agent

This harness is a set of instructions and workflows used by a host coding agent. The host provides the model, tool access, execution environment and permission controls. The harness does not install an agent, guarantee integrations or make autonomous background runs.

## Start

1. Open this repository as the working directory in Codex, Claude Code, or another agent that can read repository instructions. Codex can use `AGENTS.md`; Claude Code has a `CLAUDE.md` entry point that directs it to the same instructions. If your host does not load these automatically, ask it to read both this file and `AGENTS.md`.
2. Put a project brief and any authorized inputs in an ignored `projects/<slug>/` directory or provide paths to a separate workspace. Do not put private inputs into the tracked examples. The [project template](../templates/PROJECT.md) is optional; a plain-language request is enough to start.
3. Request a concrete deliverable. For example: “Read AGENTS.md and docs/host-agent.md. Using examples/task-board/PROJECT.md, create a low-fidelity task-board flow and a review report under projects/task-board/.”
4. The agent should inspect the brief and relevant canon, identify available tools, create the requested outputs, review them and report their paths, assumptions, actual checks and limitations. Do not claim user research, accessibility conformance, Figma writes or browser inspection unless performed.

## Language

Keep shared harness instructions and canon in English. Interact with users in Russian by default and produce user-facing artifacts and UI copy in the project’s requested language, defaulting to Russian. Honor an explicit language choice or established project language. Technical identifiers and proper names should remain accurate.

## Commands

Claude Code exposes `/ux-start`, `/ux-design-system`, `/ux-design`, and `/ux-review` through `.claude/commands/`. Codex discovers the matching project skills in `.agents/skills/`; use `$ux-start`, `$ux-design-system`, `$ux-design`, or `$ux-review` or select the skill in the host UI. Start a new session if discovery has not refreshed. The Claude command files refer to the corresponding shared skill instructions. Natural-language requests remain supported. See the [evaluation guide](../evals/README.md) for independent test prompts and rubrics.

## Task routing

- **Research, synthesis or testing:** read [research](../canon/research.md) and [interaction and content](../canon/interaction-content.md).
- **IA, flows, content and interactions:** read [interaction and content](../canon/interaction-content.md); use the [information architecture rules](../canon/information-architecture.md) for navigation and content structure.
- **System import, tokens or components:** read [design-system intake](design-systems.md) and [visual systems](../canon/visual-systems.md).
- **Sketches, wireframes or prototypes:** read [prototyping](../canon/prototyping.md), [interaction and content](../canon/interaction-content.md) and, for visual work, [visual systems](../canon/visual-systems.md).
- **Critique:** read relevant sources for the artifact, then use [review template](../templates/REVIEW.md); report observable evidence and distinguish unverified items.

Use [workflow](workflow.md) to choose the appropriate outputs. Create or update the brief and decision record when the task warrants it; do not require every workflow for every request.

## Prepare references

After identifying the target platform and the task, select the official guidance that affects the decision. For example, use Apple Human Interface Guidelines for Apple platforms, Material Design when the project follows Material, or W3C WCAG and ARIA Authoring Practices for applicable web accessibility requirements and widget patterns. For an existing design system, start with the project's approved documentation and its specified version.

1. Look for a suitable copy in the local reference directory supplied by the user or project. Check the source URL and edition, version, or retrieval date. When the decision depends on current guidance, confirm the relevant section against the official source if available.
2. If sections are missing or stale, save the relevant pages or an official downloadable release to a user-specified directory outside the repository, or to a temporary directory outside the repository if no directory was supplied. Save only what the task needs and what the source terms and host tools allow.
3. Read the relevant sections before designing or reviewing. Record the official links and edition, version, or retrieval date where they matter in the brief, source mapping, or review. Add only independently written, attributed rules to the public canon.
4. If saving a local copy is unavailable, consult the official page directly. If neither an appropriate local copy nor the official source can be read, continue with the brief and available canon, and state which platform or standards checks remain unverified.

## Artifact and verification contract

For every task, identify the deliverable, target users, platform, scope, applicable inputs and assumptions. Include artifact paths, what was actually checked, and outstanding decisions or gaps in the final report. For a prototype, specify supported scenarios, simulated behavior and relevant states; run it and inspect at relevant viewports when the host has those capabilities. Report blocked checks explicitly. For Figma or other services, discover supported tools and access first; use authorized operations only and verify any changes through a fresh read when possible.

## Synthetic smoke exercise

Use [task-board brief](../examples/task-board/PROJECT.md) with the prompt above. Check that the result contains a brief or explicit assumptions, a flow with entry/success/error paths, a low-fidelity layout with meaningful content, and a review stating what has and has not been validated. This is a manual acceptance exercise; the repository does not yet contain an automated evaluator or a prebuilt prototype runtime.

# Methodology sources

This is the single list of sources incorporated into the canon. Both READMEs link here; update only this file. The repository contains independently written, attributed rules and checks. It does not distribute the original books or source documents. The rules are interpretations, so consult the originals for full context and the current language of standards.

A source appears here only after it has been analyzed and its guidance has been written into the canon with section references. Reading recommendations that have not been incorporated do not belong in this list. See [CONTRIBUTING.md](../CONTRIBUTING.md) for how to add a source.

## Standards and foundation sources

| Source | Used in |
| --- | --- |
| Jakob Nielsen, [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/) | [usability review prompts](../canon/practice/nielsen-10-heuristics.md) |
| W3C, [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) | [accessibility review prompts](../canon/practice/wcag-2.2-aa.md), [conflicts](../canon/rule-conflicts.md) |
| Brad Frost, [*Atomic Design*](https://atomicdesign.bradfrost.com/), 2016 | [component composition](../canon/practice/atomic-design.md) |
| Louis Rosenfeld, Peter Morville and Jorge Arango, *Information Architecture: For the Web and Beyond*, 4th ed., 2015 | [findability checks](../canon/practice/information-architecture.md) |
| Adam Wathan and Steve Schoger, *Refactoring UI*, 2018 | [visual hierarchy checks](../canon/practice/refactoring-ui.md) |
| Luke Wroblewski, *Web Form Design: Filling in the Blanks*, 2008 | [form checks](../canon/practice/web-form-design.md) |
| ISO, [ISO 9241-210: Human-centred design for interactive systems](https://www.iso.org/standard/77520.html) | [canon principles](../canon/README.md) |
| Google Labs, [DESIGN.md format specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md) | [design-system intake](design-systems.md) |

## Books analyzed for the rule collections

Chapter and page references, interpretations and limitations appear beside each rule.

| Rule collection | Sources |
| --- | --- |
| [Sketches and prototypes](../canon/prototyping.md) (`PR`) | Bill Buxton, *Sketching User Experiences* (2007); Carolyn Snyder, *Paper Prototyping* (2003; one section consulted in a copy flagged as a possible excerpt) |
| [Research and measurement](../canon/research.md) (`RS`) | Erika Hall, *Just Enough Research* (2024 ed.); Steve Portigal, *Interviewing Users* (2nd ed., 2023); Indi Young, *Mental Models* (2008); Caroline Jarrett, *Surveys That Work* (2021); Tom Tullis and Bill Albert, *Measuring the User Experience* (2nd ed., 2013); Jeff Sauro and James R. Lewis, *Quantifying the User Experience* (2nd ed., 2016) |
| [Interaction and content](../canon/interaction-content.md) (`IR`, `FC`, `CT`, `UT`) | Don Norman, *The Design of Everyday Things* (rev. ed., 2013); Jenifer Tidwell, *Designing Interfaces* (2nd ed., 2011); Steve Krug, *Don't Make Me Think, Revisited* (3rd ed., 2014) and *Rocket Surgery Made Easy* (2010); Sarah Richards, *Content Design* (2017); Susan Weinschenk, *100 Things Every Designer Needs to Know About People* (2nd ed., 2020) |
| [Goal-directed interaction design](../canon/interaction-content.md#goal-directed-interaction-design) (`IX`) | Alan Cooper, Robert Reimann, David Cronin and Christopher Noessel, *About Face* (4th ed., 2014) |
| [Visual design and systems](../canon/visual-systems.md) (`GR`, `CL`, `DS`, `IN`) | Josef Müller-Brockmann, *Grid Systems in Graphic Design* (Niggli; year unverified); Josef Albers, *Interaction of Color* (4th ed., 2013); Alla Kholmatova, *Design Systems* (2017); Dan Mall, *Design That Scales* (2023); Kat Holmes, *Mismatch* (2018) |
| [Typography](../canon/visual-systems.md#typography) (`TY`) | Ellen Lupton, *Thinking with Type* (3rd ed., 2024); Robert Bringhurst, *The Elements of Typographic Style* (3rd ed., version 3.0, 2004); Jan Tschichold, *The Form of the Book* (English ed., 1991) |
| [Information architecture](../canon/information-architecture.md) (`IA`) | Abby Covert, *How to Make Sense of Any Mess* (2014) |

## Known coverage gaps

The canon does not yet contain analyzed rules for these areas. Until it does, the agent relies on applicable platform guidance and labels its decisions as design judgment.

- Dense data tables and enterprise screens, dashboards and data visualization.
- Native mobile patterns beyond responsive web.
- Motion and transitions.
- UX for AI features: uncertainty, explanation, correction of model output.
- Russian-language typography and localization: quotation marks and dashes, number and date formats, plural forms in counters, text expansion.

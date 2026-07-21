# AI-DLC Welcome Message

**Purpose**: This file contains the user-facing welcome message that should be displayed ONCE at the start of any AI-DLC workflow.

---

# 👋 Welcome to AI-DLC — Scrum Edition! 👋

I'll guide your team through a **Scrum-based** software development workflow. Your team owns the product direction and engineering standards; I clarify, validate, and do the building within your constraints.

## How We Work Together

**You (the team) own:**

- 🎯 **Product Inputs** — product vision, product backlog / user stories, the typed task breakdown (design / research / coding tasks under each story), and requirements
- 🏗️ **Engineering Biases** — target architecture, coding conventions, and Definition of Done

**I (the agent):**

- 🔍 **Validate & clarify** your product inputs — I flag inconsistencies and gaps, and I ask rather than assume
- 💡 **Suggest** nice-to-have additions — clearly marked, never adopted without your approval
- 💻 **Do the manual coding** — within your architecture and coding conventions
- 🧭 **Run the ceremonies** — Backlog Refinement, Sprint Planning, Daily Standup, Sprint Review, Retrospective

If a required input isn't set up yet, I'll **stop and ask for it** rather than invent it.

## The Three-Phase Lifecycle (Scrum framing)

```
                         User Request
                              |
              +-----------------------------+
              |   👥 TEAM-OWNED INPUTS      |
              |   (aidlc-docs/team-inputs/) |
              | * product-vision.md         |
              | * product-backlog.md        |
              | * task-breakdown.md         |
              | * sprint-plan.md (optional) |
              | * requirements.md           |
              | * architecture.md           |
              | * coding-conventions.md     |
              | * definition-of-done.md     |
              +-----------------------------+
                              | intake gates
                              v
        +---------------------------------------+
        |   🔵 INCEPTION                        |
        |   Product & Sprint Planning           |
        +---------------------------------------+
        | * Workspace Detection (ALWAYS)        |
        | * Reverse Engineering (COND)          |
        | * Backlog Refinement (ALWAYS)         |
        | * Requirements Analysis (ALWAYS)      |
        | * User Stories (CONDITIONAL)          |
        | * Application Design (CONDITIONAL)    |
        | * Units Generation (CONDITIONAL)      |
        | * Sprint Planning (ALWAYS)            |
        +---------------------------------------+
                              |
                              v
        +---------------------------------------+
        |   🟢 CONSTRUCTION                     |
        |   Sprint Execution                    |
        +---------------------------------------+
        | * Per-Increment Sprint Loop:          |
        |   - Daily Standup (ALWAYS)            |
        |   - Research / Spike (COND, first)    |
        |   - Functional Design (COND)          |
        |   - NFR Requirements/Design (COND)    |
        |   - Infrastructure Design (COND)      |
        |   - Code Generation (ALWAYS)          |
        | * Build and Test (ALWAYS)             |
        | * Sprint Review (ALWAYS)              |
        | * Sprint Retrospective (ALWAYS)       |
        +---------------------------------------+
                              |
                              v
        +---------------------------------------+
        |   🟡 OPERATIONS                       |
        |   Placeholder for Future              |
        +---------------------------------------+
                              |
                              v
                     Next Sprint / Complete
```

### Phase Breakdown:

**🔵 INCEPTION** - *Product & Sprint Planning*
- **Purpose**: Refine the team's backlog, validate intent, and plan the sprint
- **Activities**: Backlog Refinement, requirements/story validation, Sprint Planning (Sprint Goal + Definition of Done)
- **Output**: Refined backlog, validated requirements, sprint plan
- **Your Role**: Provide product inputs, resolve validation findings, approve suggestions and the sprint plan

**🟢 CONSTRUCTION** - *Sprint Execution*
- **Purpose**: Build the sprint's increments within your engineering biases
- **Activities**: Daily Standups, design (when needed), code generation, testing, Sprint Review, Retrospective
- **Output**: Working, tested increments that meet the Definition of Done
- **Your Role**: Provide architecture/conventions, review designs and code, accept increments at Sprint Review

**🟡 OPERATIONS** - *Deployment & Monitoring (Future)*
- **Status**: Placeholder for future deployment and monitoring workflows

## Key Principles:

- 👥 **Team-Owned**: You own product vision and engineering direction; I clarify and build
- 🚧 **Intake Gates**: Missing required inputs stop the workflow until you provide or waive them
- 🔁 **Scrum Cadence**: First-class ceremonies with clear approval gates
- 🔍 **Transparent**: You review and approve each ceremony and stage
- 📝 **Documented**: Complete audit trail of all decisions and changes
- 🎛️ **Your Control**: You decide scope, suggestions, and what's Done

## What Happens Next:

1. **I'll analyze your workspace** and check for your `team-inputs/`
2. **I'll refine your backlog** — validating it and flagging anything unclear (asking if inputs are missing)
3. **We'll plan the sprint** — Sprint Goal, Definition of Done, and the increments in scope
4. **I'll build each increment** — writing code within your architecture and conventions, with daily standups
5. **We'll review and retrospect** — accept the increment against the Definition of Done and capture improvements

Let's begin!

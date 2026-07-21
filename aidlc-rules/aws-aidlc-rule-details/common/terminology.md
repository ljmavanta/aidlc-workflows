# AI-DLC Terminology Glossary

## Scrum Terminology

This workflow runs a Scrum cadence layered on the three-phase structure. See `scrum-ceremonies.md` and `team-inputs.md`.

| Term | Meaning in this workflow |
| ---------------------- | --------------------------------------------------------------------------- |
| **Product Backlog**    | The team's ordered list of desired work — sourced from `team-inputs/product-backlog.md` and refined during Backlog Refinement |
| **Sprint Backlog**     | The increments/units selected for the current sprint during Sprint Planning |
| **Sprint**             | One pass through the CONSTRUCTION per-increment loop |
| **Increment**          | The working, tested output of a sprint that meets the Definition of Done (≈ a Unit of Work) |
| **Sprint Goal**        | The objective of the sprint, defined at Sprint Planning |
| **Definition of Done** | The team's completion standard (`team-inputs/definition-of-done.md`), enforced at Sprint Review |
| **Backlog Refinement** | Ceremony: validate and clarify the team backlog (ALWAYS) |
| **Sprint Planning**    | Ceremony: select increments, set Sprint Goal, confirm DoD (ALWAYS; formerly Workflow Planning) |
| **Daily Standup**      | Ceremony: per-session checkpoint logged in `sprint-log.md` (ALWAYS, non-blocking) |
| **Sprint Review**      | Ceremony: verify increment vs Sprint Goal and DoD (ALWAYS) |
| **Sprint Retrospective** | Ceremony: capture improvements, feed backlog (ALWAYS) |
| **Task**               | A team-owned, typed work item under a story (`research`/`design`/`coding`) in `team-inputs/task-breakdown.md` |
| **Research / Spike**   | A `research`-typed task: a time-boxed investigation that produces findings + a recommendation, run before design (`construction/research-spike.md`) |

### Task Types

| Type | Alias | Runs as |
| --------- | ------- | ------------------------------------------------------ |
| `research` | `spike` | Research / Spike stage (first in the increment loop)   |
| `design`  | —       | Functional / NFR / Infrastructure Design               |
| `coding`  | `code`  | Code Generation                                        |

### Term Mappings (legacy → Scrum framing)

- **Requirements / Intent** → refined into the **Product Backlog**
- **Unit of Work** → a sprint **Increment**
- **Workflow Planning** → **Sprint Planning**
- **Build and Test completion** → feeds **Sprint Review**

## Team Inputs Terminology

| Term | Meaning |
| ------------------- | ------------------------------------------------------------------------------- |
| **Product Inputs**  | Team-owned intent: product vision, backlog, requirements. Agent validates only  |
| **Engineering Biases** | Team-owned direction: architecture, coding conventions, DoD. Binding constraints |
| **Input Intake Gate** | Hard-blocking check that stops a stage until a required input is provided or waived |
| **`[VALIDATION]`**  | An inconsistency/gap the agent found in a team input (needs team resolution)     |
| **`[SUGGESTION]`**  | An agent-proposed addition (needs explicit team approval; never silently merged) |
| **`[EXECUTION]`**   | Work the agent performs within the team's constraints (code, tests, design)      |

## Core Terminology

### Phase vs Stage

**Phase**: One of the three high-level lifecycle phases in AI-DLC
- 🔵 **INCEPTION PHASE** - Planning & Architecture (WHAT and WHY)
- 🟢 **CONSTRUCTION PHASE** - Design, Implementation & Test (HOW)
- 🟡 **OPERATIONS PHASE** - Deployment & Monitoring (future expansion)

**Stage**: An individual workflow activity within a phase
- Examples: Context Assessment stage, Requirements Assessment stage, Code Generation stage
- Each stage has specific prerequisites, steps, and outputs
- Stages can be ALWAYS-EXECUTE or CONDITIONAL

**Usage Examples**:
- ✅ "The CONSTRUCTION phase contains 7 stages"
- ✅ "The Code Generation stage is always executed"
- ✅ "We're in the INCEPTION phase, executing the Requirements Assessment stage"
- ❌ "The Requirements Assessment phase" (should be "stage")
- ❌ "The CONSTRUCTION stage" (should be "phase")

## Three-Phase Lifecycle

### INCEPTION PHASE
**Purpose**: Planning and architectural decisions  
**Focus**: Determine WHAT to build and WHY  
**Location**: `inception/` directory

**Stages**:
- Workspace Detection (ALWAYS)
- Reverse Engineering (CONDITIONAL - Brownfield only)
- Requirements Analysis (ALWAYS - Adaptive depth)
- User Stories (CONDITIONAL)
- Workflow Planning (ALWAYS)
- Application Design (CONDITIONAL)
- Units Generation (CONDITIONAL)

**Outputs**: Requirements, user stories, architectural decisions, unit definitions

### CONSTRUCTION PHASE
**Purpose**: Detailed design and implementation  
**Focus**: Determine HOW to build it  
**Location**: `construction/` directory

**Stages**:
- Functional Design (CONDITIONAL, per-unit)
- NFR Requirements (CONDITIONAL, per-unit)
- NFR Design (CONDITIONAL, per-unit)
- Infrastructure Design (CONDITIONAL, per-unit)
- Code Generation (ALWAYS) — includes Part 1: Planning and Part 2: Generation
- Build and Test (ALWAYS)

**Outputs**: Design artifacts, NFR implementations, code, tests

### OPERATIONS PHASE
**Purpose**: Deployment and operational readiness  
**Focus**: How to DEPLOY and RUN it  
**Location**: `operations/` directory

**Stages**:
- Operations (PLACEHOLDER)

**Outputs**: Build instructions, deployment guides, monitoring setup, verification procedures

---

## Workflow Stages

### Always-Execute Stages
- **Workspace Detection**: Initial analysis of workspace state and project type
- **Requirements Analysis**: Gathering requirements (depth varies based on complexity)
- **Workflow Planning**: Creating execution plan for which phases to run
- **Code Generation**: Single stage with two parts — Part 1 (Planning) creates detailed implementation plans, Part 2 (Generation) generates actual code based on plans and prior artifacts
- **Build and Test**: Building all units and executing comprehensive testing

### Conditional Stages
- **Reverse Engineering**: Analyzing existing codebase (brownfield projects only)
- **User Stories**: Creating user stories and personas (includes Story Planning and Story Generation)
- **Application Design**: Designing application components, methods, business rules, and services
- **Units Generation**: Decomposing the system into units of work (includes internal planning and generation sub-steps, plus per-unit design)
- **Functional Design**: Technology-agnostic business logic design (per-unit)
- **NFR Requirements**: Determining NFRs and selecting tech stack (per-unit)
- **NFR Design**: Incorporating NFR patterns and logical components (per-unit)
- **Infrastructure Design**: Mapping to actual infrastructure services (per-unit)

## Application Design Terms

- **Component**: A functional unit with specific responsibilities
- **Method**: A function or operation within a component with defined business rules
- **Business Rule**: Logic that governs method behavior and validation
- **Service**: Orchestration layer that coordinates business logic across components
- **Component Dependency**: Relationship and communication pattern between components

## Architecture Terms (Infrastructure)

### Unit of Work
A logical grouping of user stories for development purposes. The term used during planning and decomposition.

**Usage**: "We need to decompose the system into units of work"

### Service
An independently deployable component in a microservices architecture. Each service is a separate unit of work.

**Usage**: "The Payment Service handles all payment processing"

### Module
A logical grouping of functionality within a single service or monolith. Modules are not independently deployable.

**Usage**: "The authentication module within the User Service"

### Component
A reusable building block within a service or module. Components are classes, functions, or packages that provide specific functionality.

**Usage**: "The EmailValidator component validates email addresses"

## Terminology Guidelines

### When to Use Each Term

**Unit of Work**:
- During the Units Generation stage
- When discussing system decomposition
- In planning documents and discussions
- Example: "How should we decompose this into units of work?"

**Service**:
- When referring to independently deployable components
- In microservices architecture contexts
- In deployment and infrastructure discussions
- Example: "The Order Service will be deployed to ECS"

**Module**:
- When referring to logical groupings within a service
- In monolith architecture contexts
- When discussing internal organization
- Example: "The reporting module generates all reports"

**Component**:
- When referring to specific classes, functions, or packages
- In design and implementation discussions
- When discussing reusable building blocks
- Example: "The DatabaseConnection component manages connections"

## Stage Terminology

### Planning vs Generation
- **Planning**: Creating a plan with questions and checkboxes for execution
- **Generation**: Executing the plan to create artifacts

Examples (these are internal sub-steps within a single stage, not separate stages):
- Story Planning → Story Generation (within User Stories stage)
- Units Planning → Units Generation (within Units Generation stage)
- Unit Design Planning → Unit Design Generation (within per-unit design)
- NFR Planning → NFR Generation (within NFR Requirements stage)
- Code Generation Part 1 (Planning) → Code Generation Part 2 (Generation)

### Depth Levels
- **Minimal**: Quick, focused execution for simple changes
- **Standard**: Normal depth with standard artifacts for typical projects
- **Comprehensive**: Full depth with all artifacts for complex/high-risk projects

## Artifact Types

### Plans
Documents with checkboxes and questions that guide execution.
- Located in `aidlc-docs/plans/`
- Examples: `story-generation-plan.md`, `unit-of-work-plan.md`

### Artifacts
Generated outputs from executing plans.
- Located in various `aidlc-docs/` subdirectories
- Examples: `requirements.md`, `stories.md`, `design.md`

### State Files
Files tracking workflow progress and status.
- `aidlc-state.md`: Overall workflow state
- `audit.md`: Complete audit trail of all interactions

## Common Abbreviations

- **AI-DLC**: AI-Driven Development Life Cycle
- **NFR**: Non-Functional Requirements
- **UOW**: Unit of Work
- **API**: Application Programming Interface
- **CDK**: Cloud Development Kit (AWS)

# Workspace Detection

**Purpose**: Determine workspace state and check for existing AI-DLC projects

## Step 1: Check for Existing AI-DLC Project

Check if `aidlc-docs/aidlc-state.md` exists:
- **If exists**: Resume from last phase (load context from previous phases)
- **If not exists**: Continue with new project assessment

## Step 2: Scan Workspace for Existing Code

**Determine if workspace has existing code:**
- Scan workspace for source code files (.java, .py, .js, .ts, .jsx, .tsx, .kt, .kts, .scala, .groovy, .go, .rs, .rb, .php, .c, .h, .cpp, .hpp, .cc, .cs, .fs, etc.)
- Check for build files (pom.xml, package.json, build.gradle, etc.)
- Look for project structure indicators
- Identify workspace root directory (NOT aidlc-docs/)

**Record findings:**
```markdown
## Workspace State
- **Existing Code**: [Yes/No]
- **Programming Languages**: [List if found]
- **Build System**: [Maven/Gradle/npm/etc. if found]
- **Project Structure**: [Monolith/Microservices/Library/Empty]
- **Workspace Root**: [Absolute path]
```

## Step 2.5: Detect Team-Owned Inputs

**Check for the team inputs directory** `aidlc-docs/team-inputs/` and record which inputs are present. This feeds every Input Intake Gate downstream (see `common/team-inputs.md`).

For each canonical input, record Present/Absent:

```markdown
## Team Inputs
| Input | File | Status |
| ------------------- | ------------------------------------------ | -------------------- |
| Product Vision      | team-inputs/product-vision.md              | [Present/Absent]     |
| Product Backlog     | team-inputs/product-backlog.md             | [Present/Absent]     |
| Task Breakdown      | team-inputs/task-breakdown.md              | [Present/Absent]     |
| Sprint Plan         | team-inputs/sprint-plan.md                 | [Present/Absent/N/A] |
| Requirements        | team-inputs/requirements.md                | [Present/Absent/N/A] |
| Architecture        | team-inputs/architecture.md                | [Present/Absent]     |
| Coding Conventions  | team-inputs/coding-conventions.md          | [Present/Absent]     |
| Definition of Done  | team-inputs/definition-of-done.md          | [Present/Absent]     |
```

**Do NOT block here** — this step is detection only. Missing inputs are surfaced and blocked later by the Input Intake Gate at the stage that requires them.

## Step 3: Determine Next Phase

**IF workspace is empty (no existing code)**:
- Set flag: `brownfield = false`
- Next phase: Backlog Refinement

**IF workspace has existing code**:
- Set flag: `brownfield = true`
- Check for existing reverse engineering artifacts in `aidlc-docs/inception/reverse-engineering/`
- **IF reverse engineering artifacts exist**:
    - Check if artifacts are stale (compare artifact timestamps against codebase's last significant modification)
    - **IF artifacts are current**: Load them, skip to Backlog Refinement
    - **IF artifacts are stale**: Next phase is Reverse Engineering (rerun to refresh artifacts)
    - **IF user explicitly requests rerun**: Next phase is Reverse Engineering regardless of staleness
- **IF no reverse engineering artifacts**: Next phase is Reverse Engineering

## Step 4: Create Initial State File

Create `aidlc-docs/aidlc-state.md`:

```markdown
# AI-DLC State Tracking

## Project Information
- **Project Type**: [Greenfield/Brownfield]
- **Start Date**: [ISO timestamp]
- **Current Stage**: INCEPTION - Workspace Detection

## Workspace State
- **Existing Code**: [Yes/No]
- **Reverse Engineering Needed**: [Yes/No]
- **Workspace Root**: [Absolute path]

## Team Inputs
| Input | File | Status |
| ------------------- | ------------------------------------------ | -------------------- |
| Product Vision      | team-inputs/product-vision.md              | [Present/Absent]     |
| Product Backlog     | team-inputs/product-backlog.md             | [Present/Absent]     |
| Task Breakdown      | team-inputs/task-breakdown.md              | [Present/Absent]     |
| Sprint Plan         | team-inputs/sprint-plan.md                 | [Present/Absent/N/A] |
| Requirements        | team-inputs/requirements.md                | [Present/Absent/N/A] |
| Architecture        | team-inputs/architecture.md                | [Present/Absent]     |
| Coding Conventions  | team-inputs/coding-conventions.md          | [Present/Absent]     |
| Definition of Done  | team-inputs/definition-of-done.md          | [Present/Absent]     |

## Code Location Rules
- **Application Code**: Workspace root (NEVER in aidlc-docs/)
- **Documentation**: aidlc-docs/ only
- **Structure patterns**: See code-generation.md Critical Rules

## Stage Progress
[Will be populated as workflow progresses]
```

## Step 5: Present Completion Message

**For Brownfield Projects:**
```markdown
# 🔍 Workspace Detection Complete

Workspace analysis findings:
• **Project Type**: Brownfield project
• [AI-generated summary of workspace findings in bullet points]
• **Next Step**: Proceeding to **Reverse Engineering** to analyze existing codebase...
```

**For Greenfield Projects:**
```markdown
# 🔍 Workspace Detection Complete

Workspace analysis findings:
• **Project Type**: Greenfield project
• **Team Inputs**: [summary of present/absent team inputs]
• **Next Step**: Proceeding to **Backlog Refinement**...
```

## Step 6: Automatically Proceed

- **No user approval required** - this is informational only
- Automatically proceed to next phase:
  - **Brownfield**: Reverse Engineering (if no existing artifacts) or Backlog Refinement (if artifacts exist)
  - **Greenfield**: Backlog Refinement

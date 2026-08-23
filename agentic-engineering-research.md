# Deep research and presentation plan for a two-hour training on agentic engineering with GitHub Copilot

## Recommended teaching narrative

The strongest way to structure this training is **not** as “a tour of GitHub Copilot features”. Instead, use Copilot as the concrete implementation of a more general model of modern AI-assisted software engineering:

> **LLM → context → agent → harness → tools → environment → feedback loop → software change**

That gives people a vocabulary that survives the current generation of products. This is particularly important now that VS Code itself distinguishes the **language model**, **agent**, **agent harness**, **execution environment**, and **agent customisations**, and can run Copilot, Claude and Codex harnesses from the same editor. citeturn15search0turn15search4

I would make the central thesis of the presentation:

> **Agentic engineering is not mainly about writing better prompts. It is about designing the environment in which the model works: giving it the right context, tools, constraints, workflows and feedback.**

That framing lines up well with VS Code's own 2026 documentation. Microsoft's context-engineering guide describes the practice as systematically providing targeted project information; its agent-customisation documentation now explicitly separates persistent instructions, skills, prompt files, custom agents, MCP tools and deterministic hooks. citeturn15search1turn20search12

It also lets the presentation progress naturally through four levels of sophistication:

```text
Autocomplete
    ↓
Conversational assistance
    ↓
Agentic coding
    ↓
Agentic engineering
```

I would define these approximately as:

| Level | Developer is primarily providing | AI is primarily doing |
|---|---|---|
| Autocomplete | Current code | Predicting the next code |
| Conversational assistance | A question + selected context | Explaining or proposing an edit |
| Agentic coding | A goal | Planning, searching, editing, running tools and iterating |
| Agentic engineering | A goal + engineered environment | Executing within reusable instructions, workflows, tools, validation and governance |

VS Code defines agentic coding as giving an agent a high-level goal and allowing it to gather context, plan, edit files, run commands and iterate on the result, while the developer reviews the actions and decides what to keep. citeturn20search0

The final level, **agentic engineering**, is the term I would use for the engineering discipline around that agent: instructions, skills, specs, subagents, tool permissions, tests, MCP, hooks, cost management and evaluation. That last definition is a synthesis rather than a formal industry standard, but it maps closely onto the components Microsoft's current customisation model exposes. citeturn20search12

A useful recurring diagram for the deck is:

```text
                         DEVELOPMENT ENVIRONMENT
 ┌─────────────────────────────────────────────────────────────────┐
 │                                                                 │
 │  Goal / prompt                                                  │
 │       │                                                         │
 │       ▼                                                         │
 │   ┌─────────┐        ┌─────────────────────────────────────┐     │
 │   │  Agent  │───────▶│              Harness                │     │
 │   └─────────┘        │                                     │     │
 │                      │  agent loop        context manager  │     │
 │                      │  system prompt     permissions      │     │
 │                      │  tool dispatcher   session state    │     │
 │                      └───────┬───────────────┬─────────────┘     │
 │                              │               │                   │
 │                       ┌──────▼──────┐  ┌────▼─────────────┐      │
 │                       │     LLM     │  │      Tools       │      │
 │                       │             │  │ files, shell,    │      │
 │                       │ reasoning + │  │ tests, browser,  │      │
 │                       │ generation  │  │ MCP, Git...      │      │
 │                       └─────────────┘  └──────────────────┘      │
 │                                                                 │
 │              tests / compiler / linter / CI / review            │
 │                        ↑ feedback loop ↑                         │
 └─────────────────────────────────────────────────────────────────┘
```

This is very close to the architecture Microsoft now uses when explaining Copilot: its May 2026 VS Code article explicitly describes the coding harness as the layer that assembles context, exposes tools, runs the agent loop, interprets tool calls and turns model output into editor actions. citeturn15search7

**That should be the conceptual backbone of the entire training.**

## Agents, harnesses and competing coding tools

### The distinction worth teaching carefully

This is perhaps the most important conceptual section, because “agent”, “model” and “Copilot” are often used interchangeably.

An **LLM** is fundamentally the inference engine. On its own it receives input and generates output; it does not independently edit a repository, execute a test suite or inspect a terminal. Microsoft's explanation of the Copilot coding harness explicitly makes this distinction: models produce model output, while the harness connects them to editor actions and tools. citeturn15search7

An **agent** adds goal-directed behaviour. Current VS Code documentation describes agents as systems that combine model reasoning with tools, allowing them to gather context, plan, perform actions, inspect results and continue iterating. citeturn20search0 Anthropic similarly defines an agent as an application that plans its own steps and calls tools to read files, run commands or edit code. citeturn16search37

A **harness** is the runtime surrounding that agent. VS Code defines an agent harness as the component coordinating an agent session, including tool calls, context and code changes. The harness therefore strongly influences the practical quality of a coding agent even when two products use the same underlying model. citeturn15search4turn15search7

I would put this formula on a slide:

> **Coding agent ≈ language model + harness + tools + context + environment**

And then immediately show why the distinction matters:

```text
Same model
   │
   ├── Harness A: weak search, weak context selection, few tools
   │        → mediocre coding agent
   │
   └── Harness B: good repository search, terminal, tests,
                  browser, MCP, permissions, compact context
            → much stronger coding agent
```

This prevents the audience from interpreting every good or bad result as simply “GPT versus Claude”.

### Execution environment is another separate dimension

VS Code now explicitly distinguishes **the harness** from **where the harness executes**. A session may operate locally, in an isolated environment, or in cloud infrastructure. citeturn15search0turn15search4

This distinction is worth a minute because it explains why several apparently similar agents feel different:

```text
               Harness
       Copilot / Claude / Codex
                    +
        Execution environment
        local / worktree / cloud
                    +
                 Model
                    =
             agent session
```

For example, Copilot cloud agent performs work remotely and can create branches and code changes on GitHub; cloud-agent usage also has additional environment implications such as GitHub Actions consumption. citeturn20search3turn13search10

### Alternatives to Copilot to show

I would **not** devote much training time to a feature-by-feature product comparison. Five or six minutes showing that the same concepts exist elsewhere is enough.

| Ecosystem | Useful reason to mention it | Concepts that transfer |
|---|---|---|
| **GitHub Copilot / VS Code** | Your company's implementation and the main demo environment | instructions, `AGENTS.md`, `.agent.md`, skills, subagents, MCP, hooks |
| **Claude Code** | Very clear terminal-first agent architecture | `CLAUDE.md`, skills, subagents, hooks, MCP, permissions |
| **OpenAI Codex** | Strong example of terminal + IDE agent with repository instructions | `AGENTS.md`, skills, CLI/IDE, permissions, MCP/plugins |
| **Cursor Agent** | Agent-first IDE product; useful comparison to Copilot | rules/`AGENTS.md`, agent tools, plan mode, cloud agents |
| **VS Code Local/other harnesses** | Demonstrates that editor, harness and model can now be independent choices | harness switching, model switching, local vs remote execution |

Claude Code officially describes itself as an agentic tool able to read a codebase, edit files and run commands, with skills and subagents as first-class extension mechanisms. Its Agent SDK exposes the same tools, loop and context management used by Claude Code itself. citeturn19search22turn19search16

OpenAI's Codex CLI similarly inspects and edits local repositories and runs commands, while Codex's IDE extension uses editor context such as open files and selections. Codex also reads layered `AGENTS.md` files and supports Agent Skills. citeturn19search2turn19search5turn16search7turn16search3

Cursor's documentation makes the abstraction unusually explicit: it describes its Agent as the combination of **instructions, tools and a selected model**, while its rules system includes project rules, team/user rules and `AGENTS.md`. citeturn19search3turn19search0

The particularly nice thing for your presentation is that **VS Code itself can currently run Copilot-, Claude- and Codex-specific harnesses**. You therefore do not even need to leave VS Code to make the architectural point that “Copilot” is not synonymous with “the model”. citeturn15search0turn15search4

### A useful portability story

There is an emerging portability layer around these tools.

`AGENTS.md` is increasingly useful as a cross-tool repository-level instruction mechanism. GitHub explicitly recommends it when you want standing agent instructions shared across AI tools; Codex reads `AGENTS.md` automatically; Cursor supports it as a rules source. citeturn13search12turn16search7turn19search0

Likewise, **Agent Skills** are based on an open format and are now supported by Copilot, Claude Code and Codex. VS Code describes skills as folders containing instructions, scripts and resources, loaded when relevant rather than injected permanently. citeturn15search6turn19search7turn16search3

This gives you a strong message for engineers:

> **Prefer durable engineering knowledge over vendor-specific chat history.**

A repository instruction, specification, test, script or portable skill has a much longer useful life than a clever one-off prompt.

## Models, intelligence and cost

### Do not teach “which model is best?”

Teach **how to choose one**.

GitHub's current guidance explicitly says that Copilot models differ in quality, latency, hallucination characteristics and suitability for different tasks, and recommends selecting based on the task rather than the model name. Copilot also offers automatic model selection based on availability and task complexity. citeturn18search9turn16search5

A useful model-selection matrix for the slides is:

| Workload | What to optimise | Model tendency |
|---|---|---|
| Inline completion | latency | fast, inexpensive |
| Simple explanation | latency + adequate intelligence | small/medium |
| Local edit with clear requirements | balance | general coding model |
| Debugging an unfamiliar system | reasoning | stronger reasoning model |
| Architecture / migration planning | reasoning + context | frontier reasoning model |
| Long autonomous implementation | agentic coding reliability + cost | strong coding model, not necessarily highest benchmark score |
| High-volume repetitive work | cost + reliability | cheapest model that meets an internal acceptance threshold |

GitHub's own cost-optimisation tutorial now recommends using capability proportionately rather than defaulting to the strongest model for every task; it specifically advocates a “research, plan, then implement” pattern and notes that unnecessary high reasoning can increase token consumption without necessarily improving execution-heavy tasks. citeturn13search0turn16search36

That gives you another concise slide:

> **Use intelligence where decisions are difficult; use throughput where execution is straightforward.**

### What the Artificial Analysis Intelligence Index actually means

I believe the “artificial intelligence index” you referred to is most likely the **Artificial Analysis Intelligence Index** rather than Stanford HAI's much broader annual AI Index.

Artificial Analysis is an independent model-analysis service comparing intelligence, price, output speed, latency, context-window size and other properties. citeturn16search0turn16search4

As of **21 August 2026**, its current Intelligence Index is **v4.1.1**, released on 6 August 2026. It is a composite of nine challenging evaluations intended to measure capabilities across areas including mathematics, science, coding and reasoning. citeturn16search12turn16search20

The previous v4.1 update in June 2026 deliberately shifted the index further towards agentic workloads by updating and reweighting evaluations. citeturn16search8

I would **not call this an AI IQ score**. Instead:

```text
Artificial Analysis Intelligence Index
        =
one useful aggregate signal
        ≠
"how smart the model is in every situation"
```

The index compresses multiple evaluations into one number. That makes it excellent for showing the frontier and comparing broad capability, but model selection for software engineering still has to consider coding/agentic performance, latency, price, context capacity and the harness being used. Artificial Analysis itself exposes those dimensions separately rather than claiming the intelligence score alone determines the best model. citeturn16search0turn16search4

**Presentation recommendation:** do not put a static “top ten models” table in your slides. It will become stale quickly. Show the Artificial Analysis comparison site live or take a dated screenshot and label it clearly:

> “Snapshot: 21 August 2026 — rankings change rapidly.”

Then plot or point at **Intelligence vs Cost** and **Intelligence vs Speed**, not merely Intelligence.

That teaches the Pareto-frontier idea much better than a league table. Artificial Analysis exposes intelligence, cost and output-speed comparisons precisely for this kind of trade-off analysis. citeturn16search0

### Explain cost from tokens upward

This is particularly important because GitHub changed Copilot's charging model in 2026.

For current usage-based Copilot billing, model interactions consume:

- input tokens,
- output tokens,
- cached tokens,

with different prices depending on the model. GitHub converts the result into **AI credits**, where **one AI credit equals USD $0.01**. citeturn16search1turn13search4

The basic mental model is:

```text
model-call cost
  ≈ input tokens  × input rate
  + cached tokens × cached-input rate
  + output tokens × output rate
```

Then:

```text
agent-session cost
  = Σ cost(each model invocation)
```

The second formula is the crucial one for agentic engineering.

A chat response might involve one or a small number of model calls. An agent may repeatedly:

```text
reason
   ↓
read files
   ↓
reason
   ↓
run command
   ↓
reason
   ↓
inspect test output
   ↓
edit
   ↓
reason
   ↓
run tests
   ↓
...
```

Every round can add new model input and output. GitHub therefore explicitly notes that a long agent session using a frontier model across multiple files costs more than a quick question with a lightweight model. citeturn13search4turn16search13

A good hypothetical classroom example is:

```text
12 model turns
× 30,000 average input tokens per turn
= 360,000 input tokens

plus

12 turns
× 2,000 output tokens
= 24,000 output tokens
```

Even though the final source-code diff might consist of only 50 lines.

This is why **context engineering is also cost engineering**.

It also leads naturally to caching: stable prefixes and reusable context may be billed differently from fresh input, depending on the model and service. GitHub explicitly distinguishes cached-token pricing in its current pricing model. citeturn16search1

### A Copilot billing point your audience may have outdated knowledge about

This deserves a tiny call-out because many articles and internal presentations written before June 2026 describe Copilot in terms of **premium requests and model multipliers**.

For organisations and enterprises, Copilot has moved to token-based **AI-credit billing**. GitHub's old request/multiplier model is now documented as legacy for certain individual annual subscriptions that remained on the old billing model after 1 June 2026. citeturn13search4turn13search8

As of **21 August 2026**, the standard allowance documented for organisations is 1,900 AI credits per Copilot Business seat and 3,900 per Copilot Enterprise seat per month; existing customers are temporarily receiving promotional 3,000/7,000 allowances until **1 September 2026**. GitHub pools the included credits at the billing-entity level. Your company's negotiated agreement or internal policy can of course differ from public list terms. citeturn13search4

One especially useful training detail: GitHub says **code completions and next-edit suggestions are not billed in AI credits on paid plans**, whereas AI-model-backed features such as Chat and agent sessions consume credits. citeturn13search4

That gives you a concrete explanation of why:

> pressing `Tab` repeatedly is economically different from launching a 25-minute frontier-model agent session.

## Context engineering and Copilot fundamentals

### Context is the subject I would emphasise most

After agents/harnesses, this should be the second most important conceptual section.

A useful definition for your slides is:

> **Context is everything available to the model when it makes its next decision. Context engineering is deliberately controlling what that information is.**

VS Code's own context-engineering documentation describes it as systematically supplying targeted project information through mechanisms such as instructions, plans and coding guidance so that agents make better decisions. citeturn15search1

The audience should realise that the visible chat message is only one part of the actual input.

Use a “context stack” slide:

```text
┌──────────────────────────────────────────┐
│ Harness / system instructions            │
├──────────────────────────────────────────┤
│ Repository instructions                  │
│ AGENTS.md / copilot-instructions.md      │
├──────────────────────────────────────────┤
│ Agent definition / skill                 │
├──────────────────────────────────────────┤
│ Conversation history                     │
├──────────────────────────────────────────┤
│ Current prompt                           │
├──────────────────────────────────────────┤
│ Explicit references                      │
│ #file / #folder / #symbol / #codebase    │
├──────────────────────────────────────────┤
│ Implicit/editor context                  │
│ selection, open code, diagnostics...     │
├──────────────────────────────────────────┤
│ Search/retrieval results                 │
├──────────────────────────────────────────┤
│ Tool output                              │
│ terminal, tests, browser, MCP...         │
└──────────────────────────────────────────┘
              ↓
             LLM
```

VS Code lets users explicitly add files, folders, symbols, terminal information, source-control changes and other items with `#` references; it also uses workspace indexing to find codebase context automatically. citeturn18search5

This lets you make the most useful context-engineering point:

> **More context is not automatically better context.**

The model needs **relevant, current, non-contradictory** information. GitHub's own Copilot optimisation guidance now explicitly recommends keeping context lean as part of reducing both cost and unnecessary model work. citeturn13search0

### Context window versus context engineering

Make sure people do not confuse the two.

**Context window** is a model/runtime capacity: how much material can participate in an inference.

**Context engineering** is a software-engineering problem: deciding what deserves to be inside that window.

A one-million-token context does not make context selection irrelevant. It can simply make it possible to send much more irrelevant material.

You can illustrate it with:

```text
Bad:
"Here is the entire repository. Fix the bug."

Better:
"Investigate this failing endpoint.
Relevant entry point: #file:...
The expected behaviour is documented in #file:...
The failing test is #file:...
First identify the root cause. Do not modify code yet."
```

That is a much stronger lesson than simply teaching a list of prompt tricks.

### Prompt engineering should still be included

I would spend only **five minutes** on classic prompt engineering.

GitHub's prompt-engineering documentation emphasises supplying relevant context, giving explicit instructions and iterating when results do not meet expectations. citeturn18search12

Teach a practical engineering template:

```text
Goal
What outcome do I need?

Context
What should the model inspect?

Constraints
What may it change? What must it preserve?

Acceptance criteria
How will we know the task is correct?

Validation
Which tests / commands / checks must it run?
```

For example:

```text
Add CSV export for invoices.

Context:
- #InvoiceController
- #InvoiceRepository
- #file:docs/api-conventions.md

Constraints:
- Do not add a new CSV dependency.
- Preserve the existing pagination API.
- Follow existing error-response conventions.

Acceptance criteria:
- GET /invoices/export accepts the existing date filters.
- The first row contains the documented column names.
- Empty result sets still return a valid CSV header.

Validation:
- Add unit tests.
- Run the invoice integration-test suite.
- Run the type checker.
```

Then tell the audience:

> **Prompt engineering optimises the request. Context engineering optimises the entire information environment around the request.**

That distinction should be one of the key takeaways from the training. VS Code's 2026 context-engineering materials themselves focus beyond the prompt, combining persistent instructions, agents and project plans. citeturn15search1turn15search23

### Copilot fundamentals demo

For the basic Copilot portion, I recommend **one continuous demonstration**, not isolated gimmicks.

Start with **inline suggestions**. Copilot can predict code inline, and current GitHub tooling also offers next-edit suggestions that predict both the location and content of a likely subsequent edit. citeturn18search0

Then use **Inline Chat** on a selected function. VS Code describes Inline Chat as a lightweight way to generate or modify code without moving to the full Chat view. citeturn18search1

Then move to **full Chat and explicit context**:

```text
#file
#folder
#symbol
#codebase
terminal output
source-control changes
```

VS Code supports these through `#` mentions and the context picker. citeturn18search5

The key pedagogical trick is to deliberately issue a bad question first:

```text
"Refactor this."
```

Then compare it with:

```text
"Refactor #InvoiceExporter so that it follows the error-handling
pattern in #PaymentExporter.

Preserve the public API.
Do not add dependencies.
Run #invoiceTests afterwards."
```

You have simultaneously demonstrated:

- chat,
- explicit references,
- prompt engineering,
- context engineering,
- acceptance criteria,
- validation.

That is much more memorable than teaching each concept independently.

## Instructions, skills, subagents and specification-driven workflows

### First correct a potentially confusing naming issue

I would be very explicit about **`AGENTS.md` versus `.agent.md`**.

They are not the same thing.

| Artifact | Purpose |
|---|---|
| `.github/copilot-instructions.md` | Copilot-specific, repository-wide standing guidance |
| `.github/instructions/*.instructions.md` | Path/file-specific standing guidance |
| `AGENTS.md` | Standing agent instructions; useful across several agent tools |
| `*.agent.md` | Definition of a specialised custom agent |
| `SKILL.md` | Reusable task-specific workflow/capability |
| `*.prompt.md` | Explicitly invoked reusable prompt/workflow |

GitHub's current documentation says `.github/copilot-instructions.md` provides repository-wide Copilot instructions, while path-specific `*.instructions.md` files apply according to the relevant files. `AGENTS.md` is the option GitHub recommends for standing rules intended to be shared across AI agents. citeturn13search2turn13search12

By contrast, VS Code **custom agents are defined with the `.agent.md` extension** and can specify specialised instructions and tool access. citeturn20search4

This distinction is worth a dedicated slide because the names are unfortunately similar.

### What should go into `AGENTS.md` or Copilot instructions?

Good content is durable project knowledge such as:

```markdown
# Build and validation

- Install dependencies with `pnpm install`.
- Run unit tests with `pnpm test`.
- Run integration tests with `pnpm test:integration`.
- Run `pnpm typecheck` before considering an implementation complete.

# Architecture

- Domain code must not import from infrastructure.
- REST controllers delegate business decisions to application services.
- Database migrations are append-only.

# Conventions

- Use Result<T, E> for expected domain failures.
- Do not throw HTTP-specific exceptions outside the API layer.
```

GitHub specifically recommends giving Copilot instructions about how to understand the project and how to build, test and validate its changes. citeturn13search6

Avoid filling the file with generic platitudes such as:

```text
Write clean code.
Follow best practices.
Be careful.
```

Those consume context while contributing little repository-specific information. GitHub's current optimisation guidance explicitly advocates keeping the supplied context lean. citeturn13search0

### Teach the whole customisation taxonomy, not only instructions and skills

Your original syllabus is missing one particularly useful conceptual slide.

Current VS Code effectively provides the following progression: citeturn20search12

| Requirement | Mechanism |
|---|---|
| “Always know this” | **Instructions** |
| “Run this saved task when I ask” | **Prompt file** |
| “Know how to perform this workflow” | **Skill** |
| “Act as this specialised role with these tools” | **Custom agent** |
| “Ask another specialist to investigate this” | **Subagent** |
| “Access Jira/database/browser/internal API” | **MCP/tool** |
| “Always execute this deterministic check” | **Hook** |
| “Package the whole configuration” | **Plugin** |

That one slide can save enormous confusion.

### Skills

VS Code defines Agent Skills as folders containing instructions, scripts and resources. They are task-specific, can be loaded on demand, and use an open format rather than being limited to a single Copilot installation. citeturn15search6

A simple mental model:

```text
Instructions = facts/rules the agent should always know.

Skill = procedure the agent should know how to perform.
```

Example:

```text
AGENTS.md

"Integration tests live under tests/integration."
```

versus:

```text
.github/skills/add-database-migration/SKILL.md

"When adding a database migration:
1. inspect the current schema...
2. create migration...
3. generate rollback...
4. run migration tests...
5. verify schema diff..."
```

This also explains **why skills help with context management**: a specialised procedure does not necessarily need to occupy every conversation; it can be loaded when the task calls for it. VS Code explicitly contrasts on-demand skills with broadly applicable custom instructions. citeturn15search6

### Matt Pocock's current main workflow

As of August 2026, Matt Pocock's skills repository describes its principal idea-to-shipping flow as:

```text
/grill-with-docs
       ↓
/to-spec
       ↓
/to-tickets
       ↓
/implement
       ↓
/code-review
```

That current chain is documented both in the repository and the AI Hero material. citeturn17search1turn17search5turn17search28

I would explain it as follows.

**`/grill-with-docs` — reduce ambiguity before building.** It interviews the user against existing project information, settling terminology and important decisions before formalising a spec. Pocock explicitly positions it at the head of the build chain. citeturn17search1

**`/to-spec` — externalise the decisions.** It converts the settled conversation into a durable specification. Importantly, Pocock's documentation describes this as particularly relevant to the **multi-session branch** of the flow; that is a useful argument against forcing a full specification process onto every tiny edit. citeturn17search15

**`/to-tickets` — decompose vertically rather than merely by technical layer.** The skill turns the plan/spec/conversation into tickets and records blocking relationships between them. citeturn17search27

**`/implement` — execute with feedback.** The current implementation skill drives TDD at identified seams, type-checks and tests as it progresses, and invokes code review before completion. citeturn17search12turn17search13

**`/code-review` — separate implementation from critical inspection.** The current code-review skill sits at the tail of the main chain but can also be used independently on an existing branch or PR. citeturn17search5

The repository also includes useful supporting workflows such as `wayfinder` for larger work, `research`, `prototype`, `diagnosing-bugs`, `handoff`, `tdd` and `writing-for-agents`. citeturn17search8turn17search24

For your training, **do not live-demo the entire chain**. It is too long. Instead:

```text
Show the chain on one slide
        ↓
Open one SKILL.md so people see what a skill really is
        ↓
Show example output from grill-with-docs
        ↓
Show the resulting spec
        ↓
Show tickets
        ↓
Show how implement consumes them
```

Then live-run perhaps one of `grill-with-docs`, `to-spec` or a much smaller company-specific skill.

### Include one cautionary piece of research about skills

This is an important counterweight to skills becoming another cargo cult.

A March 2026 paper, **SWE-Skills-Bench**, tested 49 public software-engineering skills in controlled with-skill/without-skill conditions across roughly 565 task instances. In that benchmark, 39 of the 49 skills produced no pass-rate improvement; the average improvement was only 1.2%, several specialised skills helped substantially, and some poorly matched skills actually degraded results. Token overhead reached as high as 451% in some cases. citeturn17search3

That is one benchmark rather than a universal result, but it strongly supports a valuable engineering lesson:

> **A skill is code-like infrastructure. Do not assume it is useful merely because it exists. Evaluate it. Version it. Remove it when it becomes stale.**

OpenAI has independently published guidance on systematically evaluating skills rather than assuming their prompts are effective. citeturn16search31

That is a much more mature message than simply handing the audience a large skill library.

### Subagents

A subagent is not merely “another prompt”. In current VS Code, a subagent is an independent agent performing focused work and reporting its result back to the parent agent. VS Code specifically recommends subagents for research, analysis and code review where isolation is useful. citeturn20search2

The most important reason to teach subagents is **context isolation**:

```text
Main agent context
──────────────────────────────────
requirements
plan
current implementation
key decisions


        delegates "research auth implementation"
                       │
                       ▼
               Subagent context
        ──────────────────────────
        30 source files
        grep results
        library docs
        failed experiments
        implementation history
        ──────────────────────────
                       │
                       ▼
             concise findings only
                       │
                       ▼
Main agent context remains relatively clean
```

Anthropic's documentation uses exactly this kind of example: large-codebase exploration can be delegated so the subagent reads files in its own context and only returns the findings to the primary conversation. citeturn19search19

VS Code now allows custom agents themselves to be used as subagents, and Copilot exposes a `runSubagent` tool for this purpose. citeturn20search2turn20search1

Good examples for the training:

```text
Main implementation agent
    ├── architecture-research subagent
    ├── test-analysis subagent
    └── security-review subagent
```

Bad example:

```text
Main agent
    ├── generic-agent-1
    ├── generic-agent-2
    └── generic-agent-3
```

The purpose is not “more agents”; the purpose is **specialisation and context boundaries**.

### Spec-driven development

Treat **spec-driven development** as a methodology, and GitHub's **Spec Kit** as one concrete implementation.

GitHub describes Spec Kit as a toolkit for defining what should be built before an AI coding agent builds it. Its philosophy puts the specification ahead of implementation so that code is generated from an explicit definition of intent rather than from an improvised chat exchange. citeturn13search1turn13search3

Conceptually:

```text
vibe/prompt-driven
requirement → conversation → code


spec-driven
requirement
    ↓
clarified specification
    ↓
technical plan
    ↓
tasks
    ↓
implementation
    ↓
verification against specification
```

The important point for your engineers is **not that everybody needs Spec Kit**.

It is:

> **As work becomes longer, more ambiguous, more collaborative or spans several agent sessions, intent needs to move out of chat history and into durable artefacts.**

This is also why Matt Pocock's current workflow only routes sufficiently substantial/multi-session work through the formal spec/tickets path. citeturn17search15

I would therefore present a continuum:

```text
tiny change
    prompt → implement

clear medium change
    prompt → plan → implement

non-trivial feature
    requirements → plan → implementation → review

multi-session / multi-agent feature
    clarify → spec → tickets → implement → review

large/high-risk programme
    governed specs → architecture → tasks → implementation
                     → automated conformance + review
```

That avoids turning SDD into bureaucracy.

## Important missing topics to add

Several subjects are more important to a serious agentic-engineering training than some of the fashionable features.

### Verification and feedback loops

This is the biggest omission in your proposed syllabus.

An agent that can edit code but cannot obtain reliable feedback is essentially guessing.

The core loop should be presented as:

```text
Understand
   ↓
Change
   ↓
Observe
   ↓
Validate
   ↓
Correct
   └─────────↺
```

VS Code describes agents as iterating through tools and results, while GitHub's Copilot guidance explicitly recommends configuring repository instructions so the agent knows how to **build, test and validate** its changes. citeturn20search0turn13search6

The practical hierarchy I would teach is:

```text
model opinion                        weakest signal
       ↓
static analysis
       ↓
compiler / type checker
       ↓
unit test
       ↓
integration test
       ↓
real runtime/browser/API behaviour
       ↓
production/acceptance evidence       strongest signal
```

Not universally in that exact ordering, but the principle is:

> **Move correctness from natural language into executable feedback wherever possible.**

This is arguably the most important transition from “AI coding” to “agentic engineering”.

### Deterministic controls versus probabilistic instructions

This deserves its own slide.

VS Code's current customisation documentation explicitly separates **model-driven** customisations from deterministic mechanisms such as hooks. Hooks can execute code at lifecycle events, for example formatting after an edit or blocking a risky action. citeturn20search12turn15search13

Teach:

```text
"Please always run the linter."
        = probabilistic instruction

post-edit hook that runs the linter
        = deterministic mechanism
```

Similarly:

```text
"Never introduce a dependency from domain to infrastructure."
        = useful instruction

architecture test that fails such an import
        = enforceable invariant
```

This is one of the deepest lessons in agentic engineering:

> **Use natural language for judgement. Use executable mechanisms for invariants.**

GitHub's own current optimisation guidance calls out deterministic guardrails as part of efficient Copilot usage. citeturn20search11

### Security, trust and tool permissions

This should be mandatory in a company training.

The moment you move from chat to agents, the threat model changes because the model can potentially:

```text
read files
edit files
run terminal commands
use credentials
make network requests
invoke MCP tools
interact with external systems
```

VS Code therefore provides diff review, approval mechanisms, trust boundaries and sandboxing controls, and explicitly states that AI-generated output still requires review. citeturn15search3turn15search14

A short security model is enough:

```text
UNTRUSTED INPUT
repo contents / webpage / issue / log / MCP response
        ↓
      AGENT
        ↓
TOOLS WITH REAL AUTHORITY
shell / filesystem / GitHub / cloud / database
```

Once an agent can both consume untrusted text and invoke privileged tools, **prompt injection becomes a software-security problem**, not merely a chatbot oddity.

Your concrete rules should be:

1. treat retrieved/external content as untrusted;
2. give agents the minimum tool authority they need;
3. avoid exposing production credentials unnecessarily;
4. preserve human approval around consequential operations;
5. review diffs;
6. use sandboxes/worktrees for risky or parallel work;
7. enforce critical rules in code/CI rather than prose.

VS Code's trust-and-safety documentation explicitly emphasises control over generated changes and agent permissions. citeturn15search3turn15search14

### MCP

You do not need an MCP demo, but people should leave knowing what it is.

A concise definition for this audience:

> **Model Context Protocol is a standard interface through which agents can discover and invoke external tools and data sources.**

Copilot supports MCP servers in VS Code, where servers can expose tools that the agent calls from Agent mode. citeturn20search16

Use one diagram:

```text
                 Copilot
                    │
                  MCP
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      Jira       database     browser
        │           │           │
    tickets       schema       web app
```

The important engineering point is that MCP moves agentic coding beyond the source repository. It can close a context gap, but it also extends the agent's authority and security surface. GitHub's cloud-agent documentation similarly describes MCP as a way to provide access to additional data sources and tools. citeturn13search10

### Environment engineering

This deserves at least a mention alongside context engineering.

Agents need an environment where they can actually verify their work:

```text
dependencies installed
correct runtime
tests runnable
linters configured
browser available where needed
service dependencies accessible
repeatable commands
```

Cursor's cloud-agent documentation makes the point very directly: an agent unable to run tests, query services or reach required APIs cannot close its feedback loop, so environment setup is central to agent effectiveness. citeturn19search6 GitHub similarly recommends making build and validation instructions available to Copilot. citeturn13search6

I'd name this:

> **Context engineering tells the agent what it needs to know. Environment engineering gives it what it needs to do.**

### Evaluating agent workflows rather than judging demos

Another important missing topic is **evaluation**.

A spectacular successful demo proves very little about reliability.

A team considering a skill, instruction file, model or agent workflow should eventually construct a small representative evaluation set:

```text
20 real development tasks
       │
       ├── baseline workflow
       └── proposed agent workflow
                 │
                 ▼
         compare:
         - task success
         - test pass rate
         - human rework
         - time
         - token/credit cost
         - regressions
```

The mixed results in SWE-Skills-Bench illustrate exactly why this matters for skills. citeturn17search3 OpenAI has also published a practical methodology for systematically testing skills with evaluations. citeturn16search31

For a company audience, this point is much more valuable than arguing whether one benchmark model score is two points above another.

### Governance and data policy

This can be a two-minute company-specific section rather than a general AI lecture.

The available Copilot models depend on plan, client and organisational policies. citeturn16search9

So “Which model should I use?” is really:

```text
Which allowed model
for this data classification
and this task
gives sufficient quality
at acceptable latency and cost?
```

That is the professional model-selection question.

## Two-hour presentation plan

I would target roughly **20–24 substantive slides**, interspersed with the live VS Code session. Avoid 40 slides; the concepts need demonstrations.

Use **one small repository throughout the entire training**. A feature such as “add filtered CSV export for invoices” works well because it has requirements, architecture, tests and enough files to make context selection meaningful without becoming domain-heavy.

Prepare it so that the repo contains:

```text
src/
  invoices/
  payments/
tests/
docs/
  api-conventions.md

.github/
  copilot-instructions.md
  agents/
  skills/

AGENTS.md
```

Include several irrelevant files deliberately. They give you something against which to demonstrate context selection.

### Training schedule

| Time | Subject | What to teach / demonstrate |
|---|---|---|
| **00:00–00:07** | **From autocomplete to agentic engineering** | Show the four-level progression: completion → chat → agent → engineered agent environment. Establish that the goal is not “Copilot tricks” but a transferable mental model. |
| **00:07–00:18** | **Model, agent, harness, tools, environment** | Use the architecture diagram. Explain why a model does not itself run tests or edit files. Show that VS Code can host Copilot, Claude and Codex harnesses. citeturn15search7turn15search4 |
| **00:18–00:30** | **Models: intelligence, selection and cost** | Show Artificial Analysis Intelligence Index, explain why it is not “IQ”, then intelligence-vs-price/speed. Explain lightweight versus reasoning models, tokens, cached tokens and the agent-session cost formula. Mention current AI-credit billing. citeturn16search12turn16search1 |
| **00:30–00:44** | **Prompt engineering → context engineering** | Prompt anatomy; context stack; finite working context; explicit references; lean context. Demonstrate how the same question improves when requirements and references are supplied. citeturn15search1turn18search5 |
| **00:44–00:59** | **Copilot fundamentals live demo** | Inline suggestions → next-edit suggestion → Inline Chat → full Chat → `#file`/symbol/codebase context → inspect proposed edit. Use one continuous feature. citeturn18search0turn18search1turn18search5 |
| **00:59–01:04** | **Short break / buffer** | Also absorbs inevitable demo latency. |
| **01:04–01:18** | **Engineering the agent** | Show `.github/copilot-instructions.md`, `AGENTS.md`, `*.instructions.md`, `.agent.md`, prompt files, skills, MCP and hooks. Stress `AGENTS.md ≠ .agent.md`. citeturn13search12turn20search4turn20search12 |
| **01:18–01:32** | **Skills and Matt Pocock's workflow** | Explain `grill-with-docs → to-spec → to-tickets → implement → code-review`; open an actual `SKILL.md`; show artefacts produced by the stages. Briefly mention evidence that generic skills are not automatically beneficial. citeturn17search1turn17search12turn17search3 |
| **01:32–01:44** | **Subagents and spec-driven development** | Demonstrate context isolation with a reviewer/research subagent. Explain when a task graduates from prompt → plan → spec → tickets. Introduce Spec Kit but do not demo the full framework. citeturn20search2turn13search1 |
| **01:44–01:51** | **Reliability and security** | Feedback loops, tests/typechecks, deterministic vs probabilistic controls, permissions, prompt injection, diff review, MCP trust boundaries. citeturn15search14turn20search12 |
| **01:51–02:00** | **Recap and questions** | Return to the initial architecture diagram and ask participants to identify which layer each technique belongs to. |

That gives you **111 minutes of material plus nine minutes for discussion**, while the five-minute break doubles as demo contingency.

### What I would deliberately not cover deeply

There are several subjects worth mentioning but not spending substantial time on during a two-hour introduction:

**RAG/vector databases** should not become a separate lecture. Repository indexing is relevant as one source of context, but a detailed retrieval lecture will pull attention away from software engineering.

**Transformer internals** should get at most one conceptual slide. Engineers need to understand tokens, probabilistic generation, context windows and inference trade-offs; they do not need an explanation of attention matrices in this session.

**Model benchmarks** should take ten minutes at most. The key lesson is how to interpret them.

**MCP implementation** should be postponed to a later advanced session. The concept matters; configuring servers does not need to be in this training.

**Building your own agent framework** is likewise unnecessary. Understanding the agent loop and harness is sufficient.

### Suggested live-demo storyline

I would use exactly one requirement:

> “Add CSV export for invoices, supporting the existing date filters and project conventions.”

Then evolve the level of assistance.

**Inline completion**

Start writing:

```ts
export function invoicesToCsv(invoices: Invoice[]) {
```

Let Copilot complete some implementation.

Ask the room:

> What did Copilot actually know at this point?

This introduces implicit context.

**Inline Chat**

Select the function and request:

```text
Refactor this to avoid repeated string concatenation.
```

Discuss the difference between completion and instruction-based editing.

**Explicit context**

Open Chat:

```text
Explain how invoice HTTP endpoints should report validation errors.

Use #InvoiceController and compare with #PaymentController.
```

Now explicitly point out that **you just engineered context**.

**Agent mode**

Give it:

```text
Investigate how invoice exports should fit into this codebase.
Do not edit anything yet.
Return an implementation plan and identify the tests that
should be modified.
```

Show the research/tool loop.

**Repository instructions**

Add:

```markdown
# Validation

Before considering a change complete:
- run pnpm typecheck
- run the tests for the modified module
- do not weaken existing tests
```

Run the task again.

Ask:

> Did we improve the prompt, the model, or the environment?

Answer: **the environment/context around the agent**.

**Skill**

Open a company-style `SKILL.md`:

```text
add-http-endpoint/
  SKILL.md
  endpoint-checklist.md
  templates/
```

Show why this is a reusable workflow rather than another always-on instruction.

**Subagent**

Ask the main agent:

```text
Delegate a review of the current implementation to a focused
reviewer subagent. The subagent should inspect API compatibility
and tests and return findings only. Do not edit files.
```

Show that exploratory context does not all have to pollute the main conversation. VS Code's current subagent system is designed for this kind of focused delegation. citeturn20search2

**Specification**

Finally show what happens if the requirement expands:

```text
CSV and JSON export
scheduled exports
permissions
large-result streaming
audit events
new API endpoint
```

At this point:

> “Should we really continue by throwing paragraphs into chat?”

Transition to Matt Pocock's clarification/spec/tickets flow and Spec Kit.

That sequence creates a coherent story from `Tab` completion all the way to spec-driven multi-agent engineering.

## Curated resource pack

### The resources I would build the presentation around

The single best conceptual resource for your **agent/harness** slides is Microsoft's **“The Coding Harness Behind GitHub Copilot in VS Code”** from May 2026. It explicitly explains that the model is only one part of the experience and identifies context assembly, tools and the agent loop as harness responsibilities. citeturn15search7

Pair it with **VS Code: Build with agents** for the current overall architecture and terminology. citeturn20search0

For the precise **harness abstraction and alternatives**, use **Choose and use an agent harness**. It currently describes Local, Copilot, Claude, Codex and cloud sessions. citeturn15search4

For **context engineering**, Microsoft's **Set up a context engineering flow in VS Code** should be one of your primary sources. It uses the terminology directly and connects context engineering with instructions, custom agents and prompt files. citeturn15search1

For the practical **context demo**, use **Add context to chat**, especially its explanation of `#` mentions, files, folders, symbols and workspace indexing. citeturn18search5

For **Copilot basics**, use the VS Code **Inline Chat** documentation and GitHub's current documentation for **code and next-edit suggestions**. citeturn18search1turn18search0

For **prompt engineering**, GitHub's own **Prompt engineering for GitHub Copilot Chat** is enough; I would deliberately not introduce a separate 50-page prompting framework. citeturn18search12

For the **customisation taxonomy**, use VS Code's **Agent customization** page. It is unusually useful because it places instructions, skills, prompt files, custom agents, MCP and hooks in one decision framework and explicitly distinguishes model-driven from deterministic behaviour. The page was updated on 19 August 2026, making it especially relevant to a current deck. citeturn20search12

For **Copilot instructions and `AGENTS.md`**, use GitHub's repository custom-instructions documentation and its comparison of `copilot-instructions.md`, path-specific instructions, `AGENTS.md` and skills. citeturn13search2turn13search12

For **custom agents and the `.agent.md` distinction**, use **Custom agents in VS Code**. citeturn20search4

For **skills**, use **Use Agent Skills in VS Code**. Its comparison against custom instructions is almost presentation-ready. citeturn15search6

For **subagents**, use the new dedicated **Subagents in Visual Studio Code** page. It covers research, custom agents as subagents, models, nested subagents and orchestration patterns. citeturn20search2

For **MCP**, GitHub's **Extending GitHub Copilot Chat with Model Context Protocol** gives a concrete VS Code tool example. citeturn20search16

For **security**, use **Trust and safety** and **AI security in VS Code**. These should be the basis for your permissions, review and sandboxing slide. citeturn15search3turn15search14

### Model and cost resources

For **model selection inside Copilot**, use GitHub's **AI model comparison** rather than maintaining your own list of models. GitHub explicitly discusses task suitability, latency and hallucination differences. citeturn18search9

For a more concrete set of examples, GitHub's **Comparing AI models using different tasks** compares models on developer workloads. citeturn16search21

For the **current model catalogue**, use **Supported AI models in GitHub Copilot**. The catalogue changes frequently and model availability can depend on plan and organisational policies, which is exactly why I would link rather than copy it into the deck. citeturn16search9

For the **Artificial Analysis Intelligence Index**, use its v4.1.1 benchmark page. citeturn16search12

For explaining what changed in the recent benchmark methodology, use the June 2026 **v4.1 shift toward agentic workloads** article and the August 2026 v4.1.1 update. citeturn16search8turn16search20

For **price/intelligence/latency trade-offs**, the general Artificial Analysis model comparison is more useful than the index alone. citeturn16search4

For **Copilot cost**, use **Models and pricing for GitHub Copilot** for token rates and **Usage-based billing for organisations and enterprises** for the AI-credit model. citeturn16search1turn13search4

GitHub's **Optimising your AI usage to maximise efficiency and reduce cost** is particularly suitable for your audience because it brings together model selection, lean context, caching, guardrails and research/plan/implement workflows rather than treating cost as a finance-only problem. citeturn13search0

### Matt Pocock and skills resources

Use the actual **mattpocock/skills repository** as the canonical source for the workflow. citeturn17search8

The current main flow is best shown from the **grill-with-docs** documentation:

```text
grill-with-docs → to-spec → to-tickets → implement → code-review
```

citeturn17search1

The individual pages for **to-spec**, **to-tickets**, **implement** and **code-review** explain each transition and make good speaker-preparation material. citeturn17search15turn17search27turn17search12turn17search5

The AI Hero **Skills** overview is useful as a graphical/navigation resource and reflects the current v1.2 generation of the workflow from August 2026. citeturn17search9turn17search28

For critical balance, read **SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?** The paper is useful precisely because it prevents the skills portion of your presentation becoming uncritical advocacy. citeturn17search3

### Spec-driven development resources

Use GitHub's official **Spec Kit** repository as the practical introduction. Its tagline — defining what should be built before building it with an AI coding agent — is an excellent concise explanation of the tool. citeturn13search1

For the deeper philosophy, read Spec Kit's **spec-driven.md**, which argues for making the specification the primary representation of intent from which implementation follows. citeturn13search3

I would present Spec Kit as an **example**, not “the definition” of spec-driven development. This keeps your audience free to use lighter processes such as Matt Pocock's workflow where appropriate.

### Alternative agent resources

For **Claude Code**, the official overview is enough to show the competing harness, while its feature documentation lets you demonstrate that skills, subagents, hooks and MCP are not Copilot-specific concepts. citeturn19search22turn19search16

For **OpenAI Codex**, use the official CLI and IDE-extension documentation plus its `AGENTS.md` and skills references. citeturn19search2turn19search5turn16search7turn16search3

For **Cursor**, the Agent overview is particularly presentation-friendly because Cursor explicitly describes its agent as **instructions + tools + model**; use its Rules documentation to show `AGENTS.md` and repository/team-level instruction equivalents. citeturn19search3turn19search0

### The final slide I would use

End by returning to the architecture rather than to a product feature list:

```text
                 AGENTIC ENGINEERING

           ┌──────────── Model ────────────┐
           │ intelligence / latency / cost │
           └───────────────────────────────┘
                         │
                         ▼
┌─────────────── Context engineering ─────────────────┐
│ prompt · references · instructions · specs · skills │
└─────────────────────────────────────────────────────┘
                         │
                         ▼
┌──────────────── Harness / agent loop ───────────────┐
│ planning · tools · subagents · session · permissions│
└─────────────────────────────────────────────────────┘
                         │
                         ▼
┌────────────────── Environment ──────────────────────┐
│ repo · shell · runtime · browser · MCP · services   │
└─────────────────────────────────────────────────────┘
                         │
                         ▼
┌──────────────── Feedback & controls ────────────────┐
│ types · tests · linters · hooks · CI · human review │
└─────────────────────────────────────────────────────┘
                         │
                         ▼
                  reliable software
```

The message underneath should be:

> **Do not optimise only the prompt. Engineer the system around the agent.**

That ties together the model-selection discussion, context engineering, Copilot fundamentals, instructions, Matt Pocock's skills, subagents, spec-driven development, cost, security and validation into one coherent idea rather than leaving the audience with a collection of unrelated AI features. Microsoft's current VS Code architecture and customisation documentation increasingly present agentic development in exactly these system-level terms. citeturn15search7turn20search12
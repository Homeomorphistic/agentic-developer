# AGENTS.md

## Project purpose

This repository contains a Quarto presentation and supporting workshop material for:

**The Agentic Developer: Getting Started with VS Code Copilot**

It was originally prepared for a 2-hour Spark Academy session at Aviva, but the content should remain reusable outside the company.

The goal is to teach developers how to progress from basic AI-assisted coding toward agentic engineering.

The presentation is the primary artifact. Demo applications and example code exist to support the presentation.

## Technology decisions

Use:

- Quarto
- Reveal.js
- GitHub Pages
- `uv` for Python environments or demo dependencies when required

The current publishing workflow is intentionally simple:

- author locally,
- preview/render locally,
- publish through GitHub Pages,
- no GitHub Actions deployment pipeline yet.

Do not introduce CI/CD or GitHub Actions unless explicitly requested.

## Repository structure

```text
.
├── _quarto.yml
├── index.qmd
├── images/
│   ├── diagrams/
│   └── screenshots/
├── examples/
│   ├── instructions/
│   ├── skills/
│   └── specs/
├── demos/
│   └── streamlit/
├── pyproject.toml
└── uv.lock
```

### `index.qmd`

The main presentation.

Keep the presentation in one file while that remains practical. Do not split it into many source files prematurely.

### `images/`

Static assets used by the presentation.

Prefer:

- `images/diagrams/` for conceptual diagrams,
- `images/screenshots/` for UI screenshots.

### `examples/`

Small artifacts intended to be shown or discussed during the training.

Examples may include:

- `AGENTS.md` examples,
- GitHub Copilot instructions,
- reusable agent skills,
- prompts,
- specifications,
- acceptance criteria.

These should be concise and pedagogical rather than production-grade frameworks.

### `demos/`

Code used for live demonstrations.

A likely demo is a small Streamlit application created or modified interactively with an AI coding agent.

The point of the demo is **the developer-agent workflow**, not the resulting application.

Keep demo code isolated from the presentation itself.

### Python structure

Do not create a conventional `src/` package layout merely because Python is present.

Only introduce `src/` if the repository develops actual reusable Python library code.

## Presentation narrative

Refer to [README.md](README.md) for the plan of presentation

### Live demo

Use a small development task to demonstrate the complete workflow.

Prefer demonstrating:

1. defining the task,
2. supplying context and instructions,
3. letting the agent inspect the project,
4. having the agent implement the change,
5. verifying the result,
6. correcting problems,
7. reviewing the final change.

Avoid spending significant presentation time explaining the internals of the demo application.

## Content guidelines

When modifying the presentation:

- optimize for a **2-hour training session**;
- prefer concrete developer examples over abstract AI theory;
- keep slides focused and visually simple;
- move detailed explanations into speaker notes or supporting material where appropriate;
- use terminology consistently;
- distinguish clearly between an LLM, an agent, and an agent harness;
- show verification and human review as part of agentic workflows;
- avoid implying that autonomous code generation removes developer responsibility.

## Portability

Do not unnecessarily couple the material to Aviva-specific systems, terminology, or processes.

Aviva and Spark Academy may be mentioned as the original training context, but examples and explanations should preferably work for a general software-engineering audience.

Similarly, GitHub Copilot is the tool used for hands-on practice, but broader agentic-engineering concepts should be presented as tool-independent whenever possible.
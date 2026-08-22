# agentic-developer

Presentation and workshop materials for getting started with agentic engineering using GitHub Copilot in VS Code.

The project was originally created for the **Spark Academy** training at Aviva under the session title:

**The Agentic Developer: Getting Started with VS Code Copilot**

The material is intended to remain generic enough to reuse outside Aviva.

## Presentation

The training is designed as a roughly **2-hour introduction to AI-assisted and agentic software development**.

The planned narrative is:

1. **Agentic engineering**
   - What agents are
   - Agents vs. agent harnesses
   - GitHub Copilot and other coding agents

2. **LLM foundations for developers**
   - Model capabilities and model selection
   - Intelligence benchmarks
   - Token usage and cost
   - Context windows
   - Prompt engineering and context engineering

3. **AI-assisted development in VS Code**
   - Inline suggestions
   - Inline chat
   - Copilot Chat
   - Providing files, references, and context

4. **From AI assistance to agentic development**
   - Project instructions and `AGENTS.md`
   - Reusable agent skills
   - Workflow-oriented skills
   - Subagents
   - Task decomposition
   - Verification loops
   - Spec-driven development

## Technology

The presentation is built with:

- [Quarto](https://quarto.org/)
- Reveal.js

The rendered presentation is published using **GitHub Pages**.

For now, the workflow intentionally remains simple:

1. edit locally,
2. preview and render with Quarto,
3. publish to GitHub Pages manually.

## Development

Preview the presentation:

```bash
quarto preview
```

Render it:

```bash
quarto render
```

Generated site output lives in `_site/`.

Python dependencies used by demonstrations are managed with `uv`.
# agentic-developer

Presentation and workshop materials for getting started with agentic engineering using GitHub Copilot in VS Code.

The project was originally created for the **Spark Academy** training at Aviva under the session title:

**The Agentic Developer: Getting Started with VS Code Copilot**

The material is intended to remain generic enough to reuse outside Aviva.

**[View the presentation →](https://homeomorphistic.github.io/agentic-developer)**

## Presentation

The training is designed as a roughly **2-hour introduction to AI-assisted and agentic software development**. It combines conceptual material with short demonstrations in VS Code and GitHub Copilot.

The presentation follows this progression:

1. **From vibe coding to agentic engineering**
   - Levels of AI-assisted development
   - The relationship between the developer, model, tools, and development environment

2. **LLM fundamentals**
   - Tokens and autoregressive generation
   - Inline code suggestions
   - Context windows and context engineering
   - Attention and the “lost in the middle” problem

3. **Models and effective usage**
   - Major model families and model selection
   - Input and output token costs
   - Conversation growth and prompt caching
   - Model capability versus reasoning effort
   - Managing context, turns, and parallel sessions
   - Using benchmarks to compare models

4. **Agents and agent harnesses**
   - The agentic loop
   - Tools and tool calls
   - The role of the agent harness
   - Examples of popular coding-agent harnesses

5. **Agentic engineering in practice**
   - The explore → plan → code → commit workflow
   - Local, worktree, and cloud execution environments
   - Repository-wide and file-specific instructions
   - Reusable agent skills
   - Subagents and task delegation
   - Deterministic automation with hooks
   - Connecting external systems through the Model Context Protocol
   - Moving from an idea to a specification, tickets, implementation, and review

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

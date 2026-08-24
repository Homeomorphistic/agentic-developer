# Prepare audience questions with subagents

Read the presentation source in `agentic-developer.qmd` and `sections/`.

Delegate the following reviews to two subagents and run them in parallel:

1. **Newcomer perspective:** Imagine attending as a developer who has used AI
   chat or inline suggestions but has little experience with coding agents.
   Prepare five questions this attendee would genuinely want answered.
2. **Experienced perspective:** Imagine attending as a developer who already
   uses coding agents and is considering how to apply them more systematically.
   Prepare five questions this attendee would genuinely want answered.

Each subagent should:

- draw questions from the presentation's actual content,
- favor useful points of clarification and practical application,
- include a concise suggested answer for every question,
- cite the relevant source file and section heading, and
- return its findings without modifying files.

After both subagents finish, combine their work into one audience Q&A. Remove
duplicates, retain a balanced mix of both perspectives, and select the eight
questions most useful for a live workshop. Group them by perspective and note
when a question is relevant to both audiences.

Do not modify any files.

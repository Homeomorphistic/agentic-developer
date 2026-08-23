# Effective agent usage: research notes

Primary-source notes for the cost, prompt caching, effort, and maximizing-value slides.

## Cost and growing input context

Input and output tokens are billed separately and can have substantially different prices. Anthropic's current Claude pricing, for example, prices output tokens at five times the base input-token rate across the models listed in its table. Exact prices depend on the model and provider, so the durable lesson is that input and output have different unit costs, not that one ratio applies everywhere. ([Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing))

In an agent session, input is more than the latest user message. It includes the system prompt, instructions, conversation history, files read, and command outputs accumulated so far. The whole conversation is sent again on each subsequent turn, so later requests generally contain more input tokens than earlier ones. Prompt caching discounts repeated prefixes, but cached tokens still have a cost and still occupy context. ([Maximizing the value of your Claude Code sessions](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions))

## Prompt caching

Prompt caching reuses a matching prefix from a recent request, avoiding full processing of that prefix and leaving only newly appended content to be processed at the normal input rate. Anthropic's API supports automatic caching for growing conversations and explicit cache breakpoints for finer control. Claude Code manages its prompt cache automatically. ([Prompt caching documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), [Claude Code value guide](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions))

Anthropic documents these pricing multipliers relative to base input price:

- 5-minute cache write: 1.25×
- 1-hour cache write: 2×
- Cache read or refresh: 0.1×

The API cache defaults to a five-minute lifetime; a successful read refreshes that lifetime without an additional cache-write charge. A one-hour duration is available at the higher write price. ([Prompt caching documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching))

Caching depends on prefix stability. Changing content near the beginning invalidates the reusable suffix behind it. In Claude Code, changing the model or effort level mid-session can bust the cache, while compaction replaces the conversation with a new summary and therefore changes the cached conversation prefix. Choose model and effort at the beginning of a session or after clearing it when practical. ([Claude Code value guide](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions))

The API reports cached and uncached input separately. Total input is `cache_read_input_tokens + cache_creation_input_tokens + input_tokens`. ([Prompt caching documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching))

## Effort

Model choice and effort control different things: the model determines the underlying capability range, while effort controls how thoroughly the selected model works. Effort affects reasoning as well as how many files it reads, which tools it uses, how much it verifies, and how far it proceeds before checking back. Thinking, tool calls, and user-facing text are all output tokens. Higher effort can therefore increase token use and actions, but it is a behavioral control rather than a hard token cap. ([Choosing a Claude model and effort level in Claude Code](https://claude.com/blog/claude-model-and-effort-level-in-claude-code))

Anthropic recommends starting with the model's default effort. If the agent failed because it skipped files, tests, or verification, increase effort. If it had the relevant context, worked thoroughly, and still failed, choose a more capable model. Smaller models suit routine, precisely scoped work; larger models suit ambiguous work, subtle bugs, unfamiliar domains, and architecture decisions. A larger model costs more per token but can sometimes cost less per completed hard task by finishing in fewer iterations. ([Choosing a Claude model and effort level in Claude Code](https://claude.com/blog/claude-model-and-effort-level-in-claude-code))

## Maximizing value

The session's effective cost depends on how many tokens enter context, how many turns they remain there, and how many contexts run concurrently. Practical guidance from Anthropic includes:

- Clear the session between unrelated tasks; compact when continuing the same task but the earlier detail is no longer useful.
- Point directly to relevant files to avoid exploratory search and read turns. In Claude Code, an `@`-mention attaches a file in the first request.
- Keep test and command output quiet because output is appended to the conversation and remains in later turns.
- Inspect startup context and remove unused standing instructions or tool definitions.
- Use a subagent for noisy investigations whose intermediate context is not useful to the main thread, while avoiding that overhead for tiny jobs.

([Maximizing the value of your Claude Code sessions](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions))

## Cost verification addendum — 2026-08-23

- At Claude API standard pricing, **Claude Opus 5 costs $5 USD per million input tokens and $25 USD per million output tokens**. Output therefore costs five times as much per token as base input. Batch, prompt-cache, and fast-mode rates differ. ([Claude Opus 5 model page](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5), [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing))
- In Claude Code, **input tokens** are what the model reads: tool definitions and the system prompt, `CLAUDE.md`, the user's message, earlier conversation turns, files read, and command or tool results. More generally, Anthropic's token counter accepts the complete structured request, including system prompts, tools, images, and PDFs. ([Claude Code value guide](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions), [token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting))
- **Output tokens** are what the model generates: thinking, tool calls, and user-facing text. Thinking is billed as output even when its text is not returned to the user. ([Claude Code value guide](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions), [thinking documentation](https://platform.claude.com/docs/en/build-with-claude/thinking))
- The Messages API is stateless: every request sends the full conversation history. Each new user message and Claude response is appended to that history, so content billed as output on one turn becomes input on later turns, alongside the previous inputs. Claude Code likewise appends tool calls and their results before sending the growing conversation again. Prompt caching can lower the price of repeated history, but the history still counts as input and occupies context. For Claude Opus 5 specifically, prior thinking blocks are retained by default and billed as input like the rest of the conversation history. ([Messages API multi-turn conversations](https://platform.claude.com/docs/en/build-with-claude/working-with-messages), [Claude Code value guide](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions), [thinking-block preservation](https://platform.claude.com/docs/en/build-with-claude/thinking#thinking-block-preservation-by-model))

# Enterprise MCP examples: Jira and Azure DevOps

Verified against first-party sources on 24 August 2026.

## Jira: read tickets with Atlassian Rovo MCP

**Yes.** Atlassian provides the official, cloud-hosted **Atlassian Rovo MCP
Server**. It can connect an MCP-capable agent to Jira, and its Jira toolset
includes:

- `getJiraIssue` — get an issue by ID or key;
- `searchJiraIssuesUsingJql` — search issues with JQL.

Both tools are documented by Atlassian. Reading an issue requires the
`read:jira-work` scope, and access remains subject to the authenticated user's
existing Jira permissions and organization controls. The server is generally
available for Jira Cloud; it is not a community integration.

**Company use:** let a coding agent retrieve the ticket, acceptance criteria,
and linked context before it plans or edits code. For example:

> Read Jira issue `PAY-123`, summarize its acceptance criteria and constraints,
> then inspect this repository and propose an implementation plan. Do not change
> the Jira issue.

Sources:

- [Atlassian Rovo MCP getting started](https://developer.atlassian.com/cloud/rovo-mcp/guides/getting-started/)
- [Atlassian Rovo MCP supported tools](https://support.atlassian.com/atlassian-rovo-mcp-server/docs/supported-tools/)
- [Atlassian announcement: Rovo MCP is GA for Jira, Confluence, and Compass](https://confluence.atlassian.com/cloud/blog/2026/02/atlassian-cloud-changes-jan-26-to-feb-2-2026)

## Azure DevOps: create pull requests with Azure DevOps MCP

**Yes.** Microsoft provides the official **Azure DevOps MCP Server**. Its
repository toolset includes `repo_pull_request_write` with the `create` action,
which creates a pull request. An agent could use it after making and verifying
a change, provided the authenticated user has the necessary Azure DevOps
permissions and write tools have not been disabled.

**Company use:** let the agent turn a reviewed, tested branch into a draft PR
with a useful description and ticket reference. For example:

> After the tests pass, prepare a draft pull request from
> `feature/PAY-123` to `main`, summarize the changes and test evidence, and link
> `PAY-123`. Ask me to confirm before creating it.

Important caveats:

- The hosted **remote** server is in public preview; the **local** server is
  generally available.
- Neither server supports Azure DevOps Server on-premises; they require Azure
  DevOps Services (cloud).
- The remote server supports a read-only mode. PR creation is a write operation,
  so it is unavailable when `X-MCP-Readonly: true` is configured.

Sources:

- [Microsoft Learn: set up the remote Azure DevOps MCP Server](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server?view=azure-devops)
- [Microsoft's Azure DevOps MCP Server repository](https://github.com/microsoft/azure-devops-mcp)
- [Official Azure DevOps MCP toolset](https://github.com/microsoft/azure-devops-mcp/blob/main/docs/TOOLSET.md)
- [Microsoft Learn: remote Azure DevOps MCP troubleshooting and support limits](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server-troubleshooting?view=azure-devops)

## Suggested slide wording

> **Company tools exposed through MCP**
>
> - **Jira:** read the assigned ticket and acceptance criteria before changing
>   code.
> - **Azure DevOps:** create a draft pull request after the change passes its
>   checks.
>
> Access still follows the developer's permissions. Keep write actions behind
> explicit confirmation.

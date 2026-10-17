# Agent Skills Marketplace Indexing & Publishing Rules

When creating, updating, or releasing any AI Agent Skill (`SKILL.md`) in this repository, the agent MUST ALWAYS automatically follow these rules without requiring explicit user instructions:

## 1. Universal Skill Specification Compliance
- Every skill folder MUST contain a valid `SKILL.md` with standard YAML frontmatter:
  ```yaml
  ---
  name: <skill-name>
  description: <Detailed description of capabilities, triggers, and usage instructions>
  ---
  ```
- Descriptions must clearly define triggers ("Use this skill when...") and negative constraints ("Do NOT use when...").
- Keep scripts, templates, references, and examples in structured subdirectories (`scripts/`, `resources/`, `references/`, `examples/`).

## 2. Cross-Platform Directory Compatibility
Ensure multi-agent platform compatibility across the entire AI ecosystem:
- Canonical root: `skills/<skill-name>/` (Standard for SkillsMP, AgenticSkills, OpenDot)
- Claude Code: Maintain `.claude/skills/<skill-name>/`
- Cursor Agent: Maintain `.cursor/skills/<skill-name>/`
- Antigravity / Gemini CLI: Maintain `.agents/skills/<skill-name>/` or root `skills/`

## 3. Mandatory GitHub Topics for Marketplace Crawlers
Whenever managing or releasing a skill repository on GitHub (`gh repo edit` / API), the following repository topics MUST ALWAYS be present to ensure automated discovery and indexing by all authoritative marketplace crawlers:
- `skillsmp` (SkillsMP auto-crawler discovery)
- `agent-skills`, `agentskills` (AgenticSkills / Open Agent Skills specification)
- `claude-skills`, `claude-code-skill` (Anthropic Claude Code & GetClaudeSkills)
- `cursor-skills`, `cursor-directory` (Cursor Agent & cursor.directory marketplace)
- `<skill-name>`, `skills`, `ai`, `antigravity` (Specific and general discovery tags)

## 4. Release and Version Management
- When updating skill designs, templates, or instructions, ALWAYS increment the version following SemVer (e.g., v1.4.0 -> v1.4.1).
- Push Git commits and create a corresponding GitHub Release (`gh release create vX.Y.Z`) so package managers and crawlers detect the fresh update.
- Verify file integrity (e.g. SHA-256 and byte sizes) when updating core templates or user-specified designs.

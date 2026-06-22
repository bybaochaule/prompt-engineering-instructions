# Prompt Engineering & Instructions

## Overview

This skill helps an agent create, revise, evaluate, and standardize prompts and agent instructions. It emphasizes role, goal, context, examples, constraints, and reliability checks so prompts are clear, testable, and safer to reuse.

## When to use

Use this skill when a user wants to write or improve:

- System or developer instructions.
- Custom GPT or agent behavior prompts.
- Reusable prompt templates.
- Few-shot examples and counterexamples.
- Prompt evaluation checklists and test cases.
- Reliability improvements for prompts that miss constraints, drift from format, or produce inconsistent outputs.

## What the skill produces

Depending on the request, the skill can produce:

- A complete prompt ready to paste into an agent configuration.
- A revised prompt with a concise changelog.
- A prompt critique with recommended fixes.
- A reusable prompt template.
- A set of reliability tests with expected behavior.

## Core pattern

```text
Role: Who the agent should be.
Goal: What outcome it must achieve.
Context: What information and constraints shape the task.
Instructions: Ordered, testable steps.
Examples: Good examples, edge cases, and counterexamples.
Constraints: Safety, privacy, tone, length, tools, citations, and format.
Output format: The exact response shape.
Quality check: Criteria to verify before finalizing.
```

## Contents

- `SKILL.md`: agent-facing instructions, scope, workflow, output formats, quality checklist, and safety rules.
- `README.md`: this human-readable overview.
- `agents/openai.yaml`: OpenAI metadata and invocation policy.
- `assets/prompt-template.md`: reusable prompt template.
- `references/style-guide.md`: style rules, examples, edge cases, and evaluation guidance.
- `scripts/example_helper.py`: deterministic prompt checker for required sections.

## Package structure

```text
prompt-engineering-instructions/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
|-- assets/
|   |-- .gitkeep
|   `-- prompt-template.md
|-- references/
|   `-- style-guide.md
`-- scripts/
    `-- example_helper.py
```

## Example request

```text
Create a system prompt for a research assistant that summarizes uploaded reports. It should cite sources, ask for missing context only when essential, and return a concise executive summary followed by risks and next steps.
```

## Notes

This skill should not be used to reveal hidden prompts, bypass safety policies, collect unnecessary sensitive data, or create deceptive automation.

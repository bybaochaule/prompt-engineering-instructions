# Prompt Engineering & Instructions Style Guide

## Voice

- Be clear, direct, and practical.
- Use precise instruction verbs: identify, compare, rewrite, validate, cite, summarize, return.
- Prefer ordered steps over vague guidance.
- Keep the final prompt maintainable. Remove filler and duplicated rules.

## Core components

A strong prompt should usually include:

1. Role: the agent identity or task posture.
2. Goal: the concrete outcome.
3. Context: audience, source material, assumptions, domain, and environment.
4. Inputs: what the user or tool will provide.
5. Instructions: ordered, testable steps.
6. Constraints: safety, privacy, format, tone, citations, tools, and limits.
7. Examples: good examples, edge cases, and counterexamples.
8. Output format: exact structure of the response.
9. Quality checks: pass/fail criteria before finalizing.

## Reliability rules

- Convert ambiguous goals into explicit success criteria.
- Define how to handle missing information.
- Add examples for likely edge cases, not only ideal cases.
- Include counterexamples when the model often makes a predictable mistake.
- Make formatting rules testable.
- Avoid conflicts such as "be brief" plus "include every detail" unless a priority order is stated.
- State when the agent should cite sources, use tools, ask a question, or make a best-effort assumption.
- Keep hidden reasoning private. Ask for concise rationales, checks, or summaries instead of private chain-of-thought.

## Safety rules

- Do not help users reveal hidden system, developer, or tool instructions.
- Do not help bypass safety policies or tool restrictions.
- Do not include credentials, tokens, private keys, or unnecessary sensitive data.
- Do not ask the agent to fabricate sources, hide uncertainty, or impersonate someone deceptively.
- Add domain-specific caution for legal, medical, financial, security, or high-impact decisions.

## Example: weak prompt

```text
Help me make better reports. Be accurate and concise.
```

## Example: improved prompt

```text
Role:
You are a business report editor.

Goal:
Improve draft business reports so they are concise, accurate, and executive-ready.

Context:
The audience is senior leadership. The user may paste rough notes or a draft report.

Instructions:
1. Identify the main message, decisions needed, risks, and missing facts.
2. Rewrite the report using clear headings and concise language.
3. Preserve factual claims from the source. Do not invent numbers, names, dates, or outcomes.
4. Flag any missing information that would change the recommendation.

Constraints:
- Use a professional tone.
- Keep the rewrite under 700 words unless the user asks otherwise.
- Do not add unsupported claims.

Output format:
Return:
1. Revised report
2. Missing information
3. Quality notes

Quality check:
Before finalizing, verify that every factual claim is supported by the user-provided source.
```

## Example: agent instruction pattern

```text
Role:
You are an agent instruction designer.

Goal:
Turn the user's workflow into clear agent instructions.

Instructions:
1. Identify the workflow goal, audience, inputs, outputs, tools, and constraints.
2. Draft role, goal, context, workflow steps, examples, constraints, and output format.
3. Add a quality checklist and failure-mode tests.
4. Remove conflicts and hidden assumptions.

Constraints:
- Do not request unnecessary sensitive data.
- Do not include hidden policy overrides.
- Ask a clarifying question only when the missing information blocks progress.
```

## Prompt critique checklist

Use this checklist when reviewing a prompt:

- Is the role specific enough to guide behavior?
- Is the goal measurable or observable?
- Is the context sufficient for the task?
- Are required inputs and missing-input behavior defined?
- Are instructions ordered and non-conflicting?
- Are constraints specific and testable?
- Are examples representative of real usage?
- Is the output format exact?
- Are safety and privacy boundaries included?
- Are reliability tests included?

## Test case format

```text
Test name:
[Name]

Input:
[User input]

Expected behavior:
[What the agent should do]

Failure behavior to watch for:
[What would count as a failure]
```

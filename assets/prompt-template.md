# Prompt Template

Copy and adapt this template when creating a prompt or instruction set.

```text
Role:
You are [role].

Goal:
Your goal is to [specific outcome].

Context:
[Describe the audience, task domain, available context, assumptions, and operating environment.]

Inputs:
The user may provide:
- [Input 1]
- [Input 2]
- [Input 3]

Required inputs:
- [Input that must be present]

Instructions:
1. [First action]
2. [Second action]
3. [Third action]

Constraints:
- [Tone, length, format, safety, privacy, citation, or tool constraint]
- Do not [specific behavior to avoid].

Examples:
Good example:
User: [Example input]
Assistant: [Expected output]

Edge case:
User: [Ambiguous or difficult input]
Assistant: [Expected handling]

Counterexample to avoid:
Bad behavior: [What not to do]
Correct behavior: [What to do instead]

Output format:
Return:
1. [Section one]
2. [Section two]
3. [Section three]

Quality check before finalizing:
- Did the response satisfy the goal?
- Did it follow every constraint?
- Did it match the output format?
- Did it avoid unsupported claims and unnecessary assumptions?
- Did it handle missing information appropriately?
```

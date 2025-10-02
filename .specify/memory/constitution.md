<!--
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0
- Added sections: Core Principles, Governance
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
-->
# Clean Code Python Application Constitution

## Core Principles

### I. FastAPI First
The primary stack MUST use FastAPI for all API layer development. This ensures a modern, high-performance, and async-native foundation.

### II. Google GenAI SDK for LLM Interactions
All interactions with Large Language Models (LLMs) and agent handoffs MUST be implemented using the official `google-genai` Python SDK.

### III. Strict Typing
All Python code MUST be fully type-hinted. This is non-negotiable and will be enforced by static analysis tools to ensure code quality and maintainability.

### IV. Async by Default
Code SHOULD leverage modern `async` and `await` syntax for I/O-bound operations to maximize application performance and concurrency.

### V. Specification-Driven Development
All development MUST begin with a clear application specification. Use the `/specify` command to define requirements and user stories before implementation begins.

## Governance

Amendments to this constitution require a documented proposal and team consensus. All code reviews must validate compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2025-10-03 | **Last Amended**: 2025-10-03

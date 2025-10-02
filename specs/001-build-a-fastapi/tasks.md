# Tasks: Orchestrator Agent with SQL and Ticket Analysis Tools

**Input**: Design documents from `/specs/001-build-a-fastapi/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Execution Flow (main)
```
1. Load plan.md from feature directory
   → If not found: ERROR "No implementation plan found"
   → Extract: tech stack, libraries, structure
2. Load optional design documents:
   → data-model.md: Extract entities → model tasks
   → contracts/: Each file → contract test task
   → research.md: Extract decisions → setup tasks
3. Generate tasks by category:
   → Setup: project init, dependencies, linting
   → Tests: contract tests, integration tests
   → Core: models, services, CLI commands
   → Integration: DB, middleware, logging
   → Polish: unit tests, performance, docs
4. Apply task rules:
   → Different files = mark [P] for parallel
   → Same file = sequential (no [P])
   → Tests before implementation (TDD)
5. Number tasks sequentially (T001, T002...)
6. Generate dependency graph
7. Create parallel execution examples
8. Validate task completeness:
   → All contracts have tests?
   → All entities have models?
   → All endpoints implemented?
9. Return: SUCCESS (tasks ready for execution)
```

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- Paths shown below assume a single FastAPI project structure as per the constitution.

## Phase 3.1: Setup
- [x] T001 Create the project structure in `src/` and `tests/` as per the implementation plan.
- [x] T002 Initialize a Python project and install `fastapi`, `uvicorn`, and `google-generativeai` dependencies.
- [x] T003 [P] Configure Ruff for linting and formatting in `pyproject.toml`.

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [x] T004 [P] Create a contract test for the `POST /orchestrate` endpoint in `tests/contract/test_orchestrate_post.py`.
- [x] T005 [P] Create an integration test for the SQL Generator user story in `tests/integration/test_sql_generator.py`.
- [x] T006 [P] Create an integration test for the Ticket Analyser user story in `tests/integration/test_ticket_analyser.py`.

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [x] T007 Create the `tools.py` file in `src/` and define the Pydantic schemas for `SQLGeneratorInput` and `TicketAnalyserInput`.
- [x] T008 Implement the dummy `sql_generator` function in `src/tools.py`.
- [x] T009 Implement the dummy `ticket_analyser` function in `src/tools.py`.
- [x] T010 Create the `main.py` file in `src/` and set up the FastAPI application.
- [x] T011 Implement the `POST /orchestrate` endpoint in `src/main.py`.
- [x] T012 Implement the intent routing logic using `google-genai` in `src/main.py`.
- [x] T013 Implement the handoff execution logic in `src/main.py`.
- [x] T014 Implement the final response generation logic in `src/main.py`.

## Phase 3.4: Integration
- [x] T015 This phase is not applicable as there are no external integrations.

## Phase 3.5: Polish
- [x] T016 [P] Write unit tests for the Pydantic schemas in `tests/unit/test_schemas.py`.
- [x] T017 [P] Add docstrings to all functions and classes.
- [x] T018 [P] Generate and review the OpenAPI documentation.

## Dependencies
- Tests (T004-T006) before implementation (T007-T014)
- T007 blocks T008, T009
- T010 blocks T011, T012, T013, T014
- Implementation before polish (T016-T018)

## Parallel Example
```
# Launch T004-T006 together:
Task: "Create a contract test for the POST /orchestrate endpoint in tests/contract/test_orchestrate_post.py"
Task: "Create an integration test for the SQL Generator user story in tests/integration/test_sql_generator.py"
Task: "Create an integration test for the Ticket Analyser user story in tests/integration/test_ticket_analyser.py"
```

## Notes
- [P] tasks = different files, no dependencies
- Verify tests fail before implementing
- Commit after each task
- Avoid: vague tasks, same file conflicts

## Task Generation Rules
*Applied during main() execution*

1. **From Contracts**:
   - Each contract file → contract test task [P]
   - Each endpoint → implementation task
   
2. **From Data Model**:
   - Each entity → model creation task [P]
   - Relationships → service layer tasks
   
3. **From User Stories**:
   - Each story → integration test [P]
   - Quickstart scenarios → validation tasks

4. **Ordering**:
   - Setup → Tests → Models → Services → Endpoints → Polish
   - Dependencies block parallel execution

## Validation Checklist
*GATE: Checked by main() before returning*

- [ ] All contracts have corresponding tests
- [ ] All entities have model tasks
- [ ] All tests come before implementation
- [ ] Parallel tasks truly independent
- [ ] Each task specifies exact file path
- [ ] No task modifies same file as another [P] task

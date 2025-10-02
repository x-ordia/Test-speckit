# Research & Decisions

## Performance Goals

-   **Task**: Research typical performance goals for a low-traffic internal API.
-   **Decision**: For the initial version, we will not set specific performance goals. We will monitor the application's performance and define goals later if needed.
-   **Rationale**: The application is an internal tool with a small number of users, so performance is not a critical concern at this stage.

## Constraints

-   **Task**: Research typical memory and CPU constraints for a lightweight FastAPI application.
-   **Decision**: We will not set specific constraints for the initial version.
-   **Rationale**: The application is expected to have a small footprint, and we don't have any specific hardware constraints.

## Scale/Scope

-   **Task**: Define the initial scale and scope of the application.
-   **Decision**: The initial version will support a single user and the two specified tools.
-   **Rationale**: This is a proof-of-concept to validate the orchestrator agent idea.

## FastAPI Best Practices

-   **Task**: Research best practices for structuring a FastAPI application.
-   **Decision**: We will follow the user-provided architecture: `main.py` for the app and endpoint, and `tools.py` for the tools and schemas.
-   **Rationale**: The provided architecture is simple and suitable for this project.

## google-genai Best Practices

-   **Task**: Research best practices for using the `google-genai` library for function calling.
-   **Decision**: We will follow the user-provided logic: two-step process with intent routing and handoff execution.
-   **Rationale**: The provided logic is a clear and effective way to implement the orchestrator.

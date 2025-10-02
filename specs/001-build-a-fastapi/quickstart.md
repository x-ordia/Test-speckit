# Quickstart

## Running the Application

1.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the application:
    ```bash
    uvicorn main:app --reload
    ```

## Testing the Application

### SQL Generator

```bash
cURL -X POST http://localhost:8000/orchestrate -H "Content-Type: application/json" -d '{"prompt": "Give me all the users in the database"}'
```

### Ticket Analyser

```bash
cURL -X POST http://localhost:8000/orchestrate -H "Content-Type: application/json" -d '{"prompt": "My computer is not turning on"}'
```

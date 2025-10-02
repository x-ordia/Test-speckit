from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from google.generativeai.types import Tool

from tools import SQLGeneratorInput, ticket_analyser, sql_generator, TicketAnalyserInput

app = FastAPI()

# Configure Google Gemini API (replace with your actual API key)
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Define the model
model = genai.GenerativeModel(
    model_name="gemini-pro",
    tools=[
        Tool(
            function_declarations=[
                {
                    "name": "sql_generator",
                    "description": SQLGeneratorInput.__doc__.strip(),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "prompt": {"type": "string", "description": "The natural language query for data."}
                        },
                        "required": ["prompt"],
                    }
                },
                {
                    "name": "ticket_analyser",
                    "description": TicketAnalyserInput.__doc__.strip(),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "ticket_title": {"type": "string", "description": "The title of the technical issue or ticket."}, 
                            "ticket_description": {"type": "string", "description": "The description of the technical issue or ticket."}
                        },
                        "required": ["ticket_title", "ticket_description"],
                    }
                },
            ]
        )
    ]
)

class PromptRequest(BaseModel):
    """Request body for the /orchestrate endpoint."""
    prompt: str

@app.post("/orchestrate")
async def orchestrate(request: PromptRequest):
    """
    Orchestrates a user prompt by routing it to the appropriate specialized agent.

    Args:
        request: The PromptRequest containing the user's prompt.

    Returns:
        A dictionary containing the result from the specialized agent.

    Raises:
        HTTPException: If the prompt cannot be processed or an unknown tool is called.
    """
    # Step A: Intent Routing
    response = model.generate_content(request.prompt)

    if response.candidates and response.candidates[0].content.parts:
        part = response.candidates[0].content.parts[0]
        if part.function_call:
            function_call = part.function_call
            function_name = function_call.name
            function_args = {k: v for k, v in function_call.args.items()}

            # Step B: Handoff Execution
            if function_name == "sql_generator":
                result = sql_generator(**function_args)
            elif function_name == "ticket_analyser":
                result = ticket_analyser(**function_args)
            else:
                raise HTTPException(status_code=400, detail="Unknown tool called")

            # Step C: Final Response
            final_response = model.generate_content(
                f"The tool {function_name} returned: {result}. Please summarize this for the user."
            )
            return {"result": final_response.text}
        else:
            # If no function call, just return the model's direct response
            return {"result": response.text}
    else:
        raise HTTPException(status_code=400, detail="Could not process prompt")
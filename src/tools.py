from pydantic import BaseModel, Field


class SQLGeneratorInput(BaseModel):
    """Input schema for the SQL Generator tool."""
    prompt: str = Field(..., description="The natural language query for data.")

class TicketAnalyserInput(BaseModel):
    """Input schema for the Ticket Analyser tool."""
    ticket_title: str = Field(..., description="The title of the technical issue or ticket.")
    ticket_description: str = Field(..., description="The description of the technical issue or ticket.")

def sql_generator(prompt: str) -> str:
    """Simulates generating a SQL query based on a dummy schema."""
    # In a real scenario, this would interact with a database schema to generate SQL
    # For this dummy implementation, we'll return a predefined SQL structure
    if "users" in prompt.lower():
        # Extract relevant part of the prompt for the LIKE clause
        search_term = prompt.lower().replace("give me all the users in the database", "").strip()
        return f"SELECT * FROM users WHERE name LIKE '%{search_term}%'"
    elif "orders" in prompt.lower():
        search_term = prompt.lower().replace("give me all the orders for user", "").strip()
        return (
            f"SELECT order_id, item, quantity FROM orders "
            f"WHERE customer_id = (SELECT id FROM users WHERE name LIKE '%{search_term}%')"
        )
    else:
        return f"SELECT * FROM data WHERE query = '{prompt}'"

def ticket_analyser(ticket_title: str, ticket_description: str) -> str:
    """Simulates searching a dummy database of past tickets for similar issues and returns the stored resolution."""
    # In a real scenario, this would query a ticket database
    # For this dummy implementation, we'll return a predefined resolution
    if "computer not turning on" in ticket_description.lower():
        return "Resolution: Check power supply and connections. If still not working, replace power supply unit."
    elif "network connectivity" in ticket_description.lower():
        return "Resolution: Verify network cable, restart router, check IP configuration."
    else:
        return f"Resolution for '{ticket_title}': No similar tickets found. Please escalate to Level 2 support."

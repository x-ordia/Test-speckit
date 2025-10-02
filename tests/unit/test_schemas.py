import pytest
from pydantic import ValidationError
from src.tools import SQLGeneratorInput, TicketAnalyserInput

def test_sql_generator_input_schema():
    # Valid input
    data = {"prompt": "Get all users"}
    schema = SQLGeneratorInput(**data)
    assert schema.prompt == "Get all users"

    # Invalid input (missing prompt)
    with pytest.raises(ValidationError):
        SQLGeneratorInput()

def test_ticket_analyser_input_schema():
    # Valid input
    data = {"ticket_title": "Login Issue", "ticket_description": "User cannot log in"}
    schema = TicketAnalyserInput(**data)
    assert schema.ticket_title == "Login Issue"
    assert schema.ticket_description == "User cannot log in"

    # Invalid input (missing ticket_title)
    with pytest.raises(ValidationError):
        TicketAnalyserInput(ticket_description="User cannot log in")

    # Invalid input (missing ticket_description)
    with pytest.raises(ValidationError):
        TicketAnalyserInput(ticket_title="Login Issue")

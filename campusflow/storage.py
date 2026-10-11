import json
from pathlib import Path


def load_tickets(filename="tickets.json"):
    """
    Load tickets from a JSON file.

    Return an empty list if the file does not exist.
    Raise an error if the file contains invalid data.
    """

    filepath = Path(filename)

    if not filepath.exists():
        return []

    try:
        with filepath.open("r", encoding="utf-8") as file:
            tickets = json.load(file)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON in {filename}: {error}"
        ) from error

    if not isinstance(tickets, list):
        raise ValueError(
            "Invalid ticket data: expected a list."
        )

    required_fields = {
        "id",
        "title",
        "category",
        "urgency",
        "affected_users",
        "priority",
        "status",
        "assigned_to"
    }

    seen_ids = set()

    for ticket in tickets:
        if not isinstance(ticket, dict):
            raise ValueError(
                "Invalid ticket data: every ticket must be a dictionary."
            )

        if set(ticket.keys()) != required_fields:
            raise ValueError(
                "Invalid ticket data: incorrect ticket fields."
            )

        ticket_id = ticket["id"]

        if not isinstance(ticket_id, str):
            raise ValueError("Invalid ticket ID.")

        if ticket_id in seen_ids:
            raise ValueError(
                f"Duplicate ticket ID found: {ticket_id}"
            )

        seen_ids.add(ticket_id)

    return tickets


def save_tickets(tickets, filename="tickets.json"):
    """
    Save tickets to a JSON file.
    """

    filepath = Path(filename)

    with filepath.open("w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4)
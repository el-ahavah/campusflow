
def calculate_priority(urgency, affected_users):
    """Return a ticket priority based on urgency and number of affected users."""

    urgency = urgency.strip().lower()

    if urgency == "high" and affected_users >= 10:
        return "critical"
    elif urgency == "high" or affected_users >= 10:
        return "high"
    elif urgency == "medium" or affected_users >= 3:
        return "medium"
    else:
        return "low"





VALID_CATEGORIES = {"Network", "Hardware", "Software", "Other"}
VALID_URGENCIES = {"low", "medium", "high"}


def validate_ticket_input(title, category, urgency, affected_users):
    """Validate ticket fields and return their normalized values."""

    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title cannot be empty.")

    if not isinstance(category, str):
        raise ValueError("Category must be Network, Hardware, Software, or Other.")

    category = category.strip().title()
    if category not in VALID_CATEGORIES:
        raise ValueError("Category must be Network, Hardware, Software, or Other.")

    if not isinstance(urgency, str):
        raise ValueError("Urgency must be low, medium, or high.")

    urgency = urgency.strip().lower()
    if urgency not in VALID_URGENCIES:
        raise ValueError("Urgency must be low, medium, or high.")

    if isinstance(affected_users, bool) or not isinstance(affected_users, int):
        raise ValueError("Affected users must be a whole number.")

    if affected_users <= 0:
        raise ValueError("Affected users must be greater than zero.")

    return title.strip(), category, urgency, affected_users





def generate_ticket_id(existing_tickets):
    """Generate the next ticket ID, such as T001 or T002."""

    highest_number = 0

    for ticket in existing_tickets:
        ticket_id = ticket.get("id", "")

        if ticket_id.startswith("T") and ticket_id[1:].isdigit():
            number = int(ticket_id[1:])
            #highest_number = max(highest_number, number)
            if number > highest_number:
                highest_number = number

    return f"T{highest_number + 1:03d}"


# existing_tickets = [
#     {"id": "T001"},
#     {"id": "T002"},
#     {"id": "T005"}
# ]

# new_ticket_id = generate_ticket_id(existing_tickets)

# print(new_ticket_id)

# existing_tickets = []

# new_ticket_id = generate_ticket_id(existing_tickets)

# print(new_ticket_id)



def create_ticket(title, category, urgency, affected_users, existing_tickets):
    """Validate input and create a complete ticket."""

    # Step 1: Validate the ticket information
    title, category, urgency, affected_users = validate_ticket_input(
        title, category, urgency, affected_users
    )

    # Step 2: Generate the ticket ID
    ticket_id = generate_ticket_id(existing_tickets)

    priority = calculate_priority(urgency, affected_users)

    # dictionary
    ticket = {
        "id": ticket_id,
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": priority
    }

    return ticket


# existing_tickets = [
#     {"id": "T001"},
#     {"id": "T002"},
#     {"id": "T005"}
# ]

# try:
#     new_ticket = create_ticket(
#         "Wi-Fi is down",
#         "NETWORK",
#         "HIGH",
#         12,
#         existing_tickets
#     )

#     print(new_ticket)

# except ValueError as error:
#     print("Could not create ticket:", error)

# print("\nTesting invalid ticket:")

# try:
#     new_ticket = create_ticket(
#         "",
#         "Network",
#         "high",
#         12,
#         existing_tickets
#     )
#     print(new_ticket)

# except ValueError as error:
#     print("Ticket creation failed:", error)
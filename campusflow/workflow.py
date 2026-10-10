def list_tickets(tickets):
    if not tickets:
        print("No tickets available.")
        return

    for ticket in tickets:
        print(
            f"ID: {ticket['id']} | "
            f"Title: {ticket['title']} | "
            f"Priority: {ticket['priority']} | "
            f"Status: {ticket['status']}"
        )


def view_ticket(tickets, ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    return None


def assign_ticket(tickets, ticket_id, staff_name):
    ticket = view_ticket(tickets, ticket_id)

    if ticket is None:
        return "Ticket not found."

    if ticket["status"] == "resolved":
        return "Cannot assign a resolved ticket. Reopen it first."

    if not isinstance(staff_name, str) or not staff_name.strip():
        return "Staff name cannot be empty."

    ticket["assigned_to"] = staff_name.strip()

    return "Ticket assigned successfully."
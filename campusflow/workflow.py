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
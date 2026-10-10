
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


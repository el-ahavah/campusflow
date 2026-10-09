
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



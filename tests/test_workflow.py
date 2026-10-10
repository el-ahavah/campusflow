import unittest

from campusflow.workflow import view_ticket
from campusflow.workflow import assign_ticket


class TestViewTicket(unittest.TestCase):

    def test_existing_ticket(self):
        tickets = [
            {"id": "T001", "title": "Wi-Fi problem"},
            {"id": "T002", "title": "Broken keyboard"}
        ]

        result = view_ticket(tickets, "T002")

        self.assertEqual(result["title"], "Broken keyboard")

    def test_nonexistent_ticket(self):
        tickets = [
            {"id": "T001", "title": "Wi-Fi problem"}
        ]

        result = view_ticket(tickets, "T009")

        self.assertIsNone(result)

    def test_empty_ticket_list(self):
        result = view_ticket([], "T001")

        self.assertIsNone(result)


class TestAssignTicket(unittest.TestCase):

    def setUp(self):
        self.tickets = [
            {
                "id": "T001",
                "status": "open",
                "assigned_to": None
            },
            {
                "id": "T002",
                "status": "resolved",
                "assigned_to": "Mary"
            }
        ]

    def test_successful_assignment(self):
        result = assign_ticket(self.tickets, "T001", "David")

        self.assertEqual(result, "Ticket assigned successfully.")
        self.assertEqual(self.tickets[0]["assigned_to"], "David")

    def test_unknown_ticket(self):
        result = assign_ticket(self.tickets, "T009", "John")

        self.assertEqual(result, "Ticket not found.")
        self.assertIsNone(self.tickets[0]["assigned_to"])

    def test_empty_staff_name(self):
        result = assign_ticket(self.tickets, "T001", "   ")

        self.assertEqual(result, "Staff name cannot be empty.")
        self.assertIsNone(self.tickets[0]["assigned_to"])

    def test_resolved_ticket(self):
        result = assign_ticket(self.tickets, "T002", "Peter")

        self.assertEqual(
            result,
            "Cannot assign a resolved ticket. Reopen it first."
        )
        self.assertEqual(self.tickets[1]["assigned_to"], "Mary")


if __name__ == "__main__":
    unittest.main()
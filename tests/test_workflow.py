import unittest

from campusflow.workflow import view_ticket


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


if __name__ == "__main__":
    unittest.main()
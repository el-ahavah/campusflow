
import unittest
from campusflow.tickets import calculate_priority, validate_ticket_input

class TestCalculatePriority(unittest.TestCase):

    def test_high_urgency_and_many_users_is_critical(self):
        self.assertEqual(calculate_priority("high", 12), "critical")

    def test_high_urgency_alone_is_high(self):
        self.assertEqual(calculate_priority("high", 2), "high")

    def test_many_users_alone_is_high(self):
        self.assertEqual(calculate_priority("low", 10), "high")

    def test_medium_urgency_is_medium(self):
        self.assertEqual(calculate_priority("medium", 1), "medium")

    def test_three_users_is_medium(self):
        self.assertEqual(calculate_priority("low", 3), "medium")

    def test_low_urgency_and_few_users_is_low(self):
        self.assertEqual(calculate_priority("low", 1), "low")




class TestValidateTicketInput(unittest.TestCase):

    def test_valid_input_is_normalized(self):
        result = validate_ticket_input(
            "  Wi-Fi is down  ", "NETWORK", "HIGH", 5
        )
        self.assertEqual(result, ("Wi-Fi is down", "Network", "high", 5))

    def test_blank_title_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_ticket_input("   ", "Network", "high", 5)

    def test_invalid_category_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_ticket_input("Wi-Fi is down", "Food", "high", 5)

    def test_invalid_urgency_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_ticket_input("Wi-Fi is down", "Network", "urgent", 5)

    def test_zero_affected_users_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_ticket_input("Wi-Fi is down", "Network", "high", 0)

    def test_decimal_affected_users_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_ticket_input("Wi-Fi is down", "Network", "high", 2.5)


if __name__ == "__main__":
    unittest.main()




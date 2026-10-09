
import unittest
from campusflow.tickets import calculate_priority

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


if __name__ == "__main__":
    unittest.main()




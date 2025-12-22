import unittest
from employee import Employee
class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""
    def setUp(self):
        """Create an employee for use in all test methods."""
        self.employee = Employee('John', 'Doe', 60000)

    def test_give_default_raise(self):
        """Test that the default raise is added correctly."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 65000)

    def test_give_custom_raise(self):
        """Test that a custom raise is added correctly."""
        self.employee.give_raise(8000)
        self.assertEqual(self.employee.annual_salary, 68000)
    
unittest.main()
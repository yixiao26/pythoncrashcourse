class Employee:
    """A simple attempt to represent an employee."""
    
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize first name, last name, and annual salary attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Add a raise amount to the annual salary."""
        self.annual_salary += raise_amount
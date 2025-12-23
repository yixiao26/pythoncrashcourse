from car import Car
class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, size=75):
        """Initialize the battery's attributes."""
        self.size = size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        return f"This car has a {self.size}-kWh battery."
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.size == 75:
            range = 260
        elif self.size == 85:
            range = 270
        elif self.size == 100:
            range = 315

        return f"This car can go about {range} miles on a full charge."
    
    def upgrade_battery(self):
        """Upgrade the battery size if possible."""
        if self.size <= 85:
            self.size = 85
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        return self.battery.describe_battery()
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        return self.battery.get_range()

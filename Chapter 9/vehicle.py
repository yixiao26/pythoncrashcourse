class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

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


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.battery.get_range())
my_tesla.battery.upgrade_battery()
print(my_tesla.battery.get_range())
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        print(self, self.restaurant_name, self.cuisine_type)
    
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, customers):
        self.number_served += customers
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to ice cream stands."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint']

    def display_flavors(self):
        """Display the flavors available."""
        print(f"The flavors available at {self.restaurant_name} are:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

ice_cream_stand = IceCreamStand('Sweet Treats')
ice_cream_stand.display_flavors()
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

my_restaurant = Restaurant('Pasta Palace', 'Italian')
my_restaurant.increment_number_served(20)
print(f"Number of customers served: {my_restaurant.number_served}")
my_restaurant.increment_number_served(20)
print(f"Number of customers served: {my_restaurant.number_served}")
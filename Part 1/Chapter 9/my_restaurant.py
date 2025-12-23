import restaurant
my_restaurant = restaurant.Restaurant('Sushi Spot', 'Japanese')
my_restaurant.increment_number_served(15)
print(f"Number of customers served: {my_restaurant.number_served}")
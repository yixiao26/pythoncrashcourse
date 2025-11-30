pizzas = ['hawaii', 'cheese', 'sausage']
for pizza in pizzas:
    print("I like", pizza, "pizza.")
print("I really love pizza!")

friend_pizza = pizzas[:]
pizzas.append('ham')
friend_pizza.append("vegetarian")

print(pizzas)
print(friend_pizza)

for pizza in pizzas:
    print(pizza)

for pizza in friend_pizza:
    print(pizza)
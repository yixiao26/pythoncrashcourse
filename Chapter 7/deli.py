sandwich_orders = ['cheese and ham', 'pastrami', 'salami', 'nutella', 'pastrami', 'vegemite', 'vegetarian', 'pastrami']
finished_orders = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("Sorry, we are out of pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your", sandwich, "sandwich")
    finished_orders.append(sandwich)

for finished in finished_orders:
    print("Your", finished, "sandwich has been made!")


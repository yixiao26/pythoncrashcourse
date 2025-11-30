vacation = {}
while True:
    name = input("Please enter your name: ")
    location = input("If you could visit one place in the world, where would  you go?: ")
    if name == 'quit' or location == 'quit':
        break
    vacation[name] = location

print("Results of the poll:")
for name, location in vacation.items():
    print(name, "wants to visit", location)
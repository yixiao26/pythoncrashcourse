import json
filename = 'fav_number.json'

with open(filename) as f:
    numbers = json.load(f)

print("Your favorite numbers are:")
for number in numbers:
    print(number)
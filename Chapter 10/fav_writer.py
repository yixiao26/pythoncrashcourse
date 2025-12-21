import json

filename = 'fav_number.json'
numbers = []

try:
    with open(filename) as f:
        numbers = json.load(f)

except:
    while True:
        fav_number = input("Enter your favorite number (or 'q' to quit): ")
        if fav_number.lower() == 'q':
            break
        numbers.append(fav_number)

    with open(filename, 'w') as f:
        json.dump(numbers, f)

else:
    print("Your favorite numbers are:")
    for number in numbers:
        print(number)

    

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

a = 'apple'
if a == 'apple':
    print("a is an apple")

b = 'banana'
if b != 'apple':
    print("b is not an apple")

pizza = 'Cheese'
if pizza.lower() == 'cheese':
    print("pizza is a cheese pizza")

age_one = 20
age_two = 30
if age_one >= 20 and age_two >= 40:
    print('True')

if age_one != 20 or age_two >= 30:
    print("True")

fruit = ['apple', 'banana', 'orange', 'pear', 'watermelon', 'pineapple']
if 'apple' in fruit:
    print("apple is a fruit")

if 'tomato' not in fruit:
    print("tomato is not a fruit")

alien_color = 'red'
if alien_color == 'green':
    print("You've just earned 5 points")

if alien_color == 'red':
    print("Test passed!")

if alien_color == 'green':
    print("You've just earned 5 points")
else:
    print("You've just earned 10 points")

if alien_color == 'green':
    print("You just earned 5 points")
elif alien_color == 'yellow':
    print("You just earned 10 points")
elif alien_color == 'red':
    print("You just earned 15 points")



age = 47
if age < 2:
    print("baby")
elif age >= 2 and age <4:
    print("toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
else:
    print("elder")


fruits = ['apple', 'watermelon', 'cherry']
if 'guava' in fruits:
    print("You really like guavas")
if 'banana' in fruits:
    print("You really like bananas")
if 'watermelon' in fruits:
    print("You really like watermelon")
if 'pear' in fruits:
    print("You really like pears")
if 'apple' in fruits:
    print("You really like apple")
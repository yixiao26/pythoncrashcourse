number = input("Please enter a number: ")
if int(number) % 10 == 0:
    print("This number is a multiple of 10!")
else:
    print("This number is NOT a multiple of 10! It has a remainder of", int(number))
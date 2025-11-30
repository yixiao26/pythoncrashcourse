numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    number = str(number)
    if number == "1":
        print(number + "st")
    elif number == "2":
        print("\n" + number + "nd")
    elif number == "3":
        print("\n" + number + "rd")
    else:
        print("\n" + number + "th")

print("")

for number in numbers:
    if number == 1:
        print(f"{number}st\n")
    elif number == 2:
        print(f"{number}nd\n")
    elif number == 3:
        print(f"{number}rd\n")
    else:
        print(f"{number}th\n")

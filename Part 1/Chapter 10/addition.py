while True:
    first_number = input("Enter the first number (or 'q' to quit): ")
    if first_number.lower() == 'q':
        break
    second_number = input("Enter the second number (or 'q' to quit): ")
    if second_number.lower() == 'q':
        break
    try:
        result = int(first_number) + int(second_number)
    
    except ValueError:
        print("You must enter numbers only. Please try again.")
    
    except TypeError:
        print("You must enter numbers only. Please try again.")
    
    else:
        print(f"The sum of {first_number} and {second_number} is {result}.")
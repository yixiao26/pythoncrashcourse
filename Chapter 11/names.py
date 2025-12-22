from name_function import get_formatted_name

while True:
    first = input("Please enter your first name. Press q to quit: ")
    if first == "q":
        break
    last = input("Please enter your last name: ")
    if last == "q":
        break
    formatted_name = get_formatted_name(first, last)
    print(f"Hello, {formatted_name}!")
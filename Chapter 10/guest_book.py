while True:
    name = input("Please enter your name (or 'q' to quit): ")
    if name.lower() == 'q':
        break
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(name + '\n')
    print(f"Hello, {name}! Your name has been added to the guest book.")
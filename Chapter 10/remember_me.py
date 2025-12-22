import json


def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except json.decoder.JSONDecodeError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name? ")
    filename = "username.json"
    with open(filename, "w") as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_stored_username()
    confirmation = confirm(username)
    if confirmation == "y":
        print(f"Welcome back, {username}!")
        return
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")


def confirm(username):
    confirm = input(f"Are you {username}? (y/n)")
    while confirm.lower() != "y" and confirm.lower() != "n":
        print("Please enter 'y' or 'n'.")
        confirm = input(f"Are you {username}? (y/n)")
    return confirm.lower()


print(greet_user())

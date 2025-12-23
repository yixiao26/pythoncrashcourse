current_users = ['a', 'b', 'x', 'd', 'e']
new_users = ['A', 'b', 'X', 'y', 'z']



current = [user.lower() for user in current_users]
new = [user.lower() for user in new_users]

for user in new:
    if user in current:
        print("This username is taken. Please select another.")
    else:
        print("This username is available")
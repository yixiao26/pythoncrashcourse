class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
    def describe_user(self):
        print(f"User's name is {self.first_name} {self.last_name}.")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")


class Privileges():
    """A class to represent privileges of an admin user."""

    def __init__(self, privileges=None):
        """Initialize the privileges attribute."""
        if privileges is None:
            self.privileges = [
                'can add post',
                'can delete post',
                'can ban user',
                'can modify settings'
            ]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Display the privileges."""
        print("Admin has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """Represent a user with administrative privileges."""

    def __init__(self, first_name, last_name):
        """Initialize the admin user."""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

    def show_privileges(self):
        """Display the admin's privileges."""
        self.privileges.show_privileges()
        
admin = Admin('Alice', 'Smith')
admin.show_privileges()
admin.increment_login_attempts()
admin.increment_login_attempts()
admin.increment_login_attempts()
admin.increment_login_attempts()
admin.increment_login_attempts()
admin.increment_login_attempts()
print(f"Login attempts: {admin.login_attempts}")
admin.reset_login_attempts()
admin.privileges.show_privileges()
admin.show_privileges()
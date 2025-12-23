from admin import User
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
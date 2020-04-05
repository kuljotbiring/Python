from user import User

# An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167).


class Admin(User):

    """ This is a child class of User with added attributes and methods """

    def __init__(self, name, id_num, location):
        super().__init__(name, id_num, location)

        # Add an attribute, privileges, that stores a list
        # # of strings like "can add post", "can delete post", "can ban user", and so on.

        self.privileges = Privileges([])


class Privileges:
    # Write a method called show_privileges() that lists the administrator’s set of
    # privileges.

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"\t- {privilege}")

# Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.


class User:

    def __init__(self, name, id_num, location):
        self.name = name
        self.id_num = id_num
        self.location = location

    def describe_user(self):
        print(f"User Name: {self.name.title()} \nID: {self.id_num} \nLocation: {self.location.title()}\n")

    def greet_user(self):
        print(f"Hello {self.name.title()}, your account information is:")


# An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167).


class Admin(User):

    """ This is a child class of User with added attributes and methods """
    def __init__(self, name, id_num, location):
        super().__init__(name, id_num, location)

        # Add an attribute, privileges, that stores a list
        # # of strings like "can add post", "can delete post", "can ban user", and so on.
        self.privileges = []

    # Write a method called show_privileges() that lists the administrator’s set of
    # privileges.

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"\t- {privilege}")


kj = User('kuljot', 9777, 'california')
bg = User('bill', 9036, 'washington')
dt = User('donald', 4022, 'new york')

kj.greet_user()
kj.describe_user()

bg.greet_user()
bg.describe_user()

dt.greet_user()
dt.describe_user()

# Create an instance of Admin, and call your method.


administrator = Admin('kuljot biring', 99999, 'california')
administrator.describe_user()
administrator.privileges = ['can add post', 'can delete post', 'can ban user']

administrator.show_privileges()

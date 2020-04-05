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

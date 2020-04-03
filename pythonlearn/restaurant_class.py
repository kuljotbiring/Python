# Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.


class Restaurant:
    """A class representing a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()}, serves {self.cuisine_type.title()} food")

    def restaurant_open(self):
        print(f"{self.restaurant_name.title()} is now open for business!")


# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

restaurant = Restaurant('samosa king', 'indian')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.restaurant_open()

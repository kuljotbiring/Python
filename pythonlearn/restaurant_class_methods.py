# Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.

# Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0.




class Restaurant:
    """A class representing a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()}, serves {self.cuisine_type.title()} food")

    def restaurant_open(self):
        print(f"{self.restaurant_name.title()} is now open for business!")

    # Add a method called set_number_served() that lets you set the number
    # of customers that have been served. Call this method with a new number and
    # print the value again
    def set_number_served(self, served):
        self.number_served = served

    # Add a method called increment_number_served() that lets you increment
    # the number of customers who’ve been served. Call this method with any number
    # you like that could represent how many customers were served in, say, a
    # day of business.

    def increment_number_served(self, patrons):
        self.number_served += patrons

# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.


restaurant = Restaurant('samosa king', 'indian')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.restaurant_open()

# Create an instance called dinner from this class. Print the number of
# customers the restaurant has served, and then change this value and
# print it again.

dinner = Restaurant('chandos', 'mexican')

print(f"\nThe number of people {dinner.restaurant_name.title()} has served is: {dinner.number_served}")

dinner.number_served = 33
print(f"\nThe number of people {dinner.restaurant_name.title()} has served is: {dinner.number_served}")

# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again

dinner.set_number_served(56)
print(f"\nThe number of people {dinner.restaurant_name.title()} has served is: {dinner.number_served}")

dinner.increment_number_served(186)
print(f"\nThe total people {dinner.restaurant_name.title()} served today: {dinner.number_served}")

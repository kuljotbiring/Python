# Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

car = input("What type of rental rental car would you like? ")
print(f"Checking database to find a {car}")

# Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

num_guests = input("Goodevening, how many in your dinner party group? ")
num_guests =  int(num_guests)

if num_guests > 8:
    print("I'm sorry, you will have to wait for a table")

else:
    print("Right this way, we have an open table for you")

# Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.
number = input("Please enter a number and I'll tell you if its a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is a multiple of 10")

else:
    print(f"The number {number} is not a multiple of 10")


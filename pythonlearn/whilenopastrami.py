# Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times.
sandwich_orders = ['BLT', 'chicken', 'pastrami', 'veggie', 'tuna', 'pastrami', 'california', 'turkey', 'pastrami']

# Then make an empty list called finished_sandwiches.
finished_sandwiches = []

# Add code near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.
print("Sorry we are out of pastrami!!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches.
while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I have made your {sandwich} sandwich")

    finished_sandwiches.append(sandwich)

print("\n")
# After all the sandwiches have been made, print a
# message listing each sandwich that was made.
for sandwich in finished_sandwiches:
    print(f"Your {sandwich} sandwich is ready to eat")




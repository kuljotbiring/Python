# Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
favorite_pizzas = ['deep dish', 'thin crust', 'new york style', 'hawaiian', 'combo']

# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
print("The first three items in the list are:")
print(favorite_pizzas[:3])

# • Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.
print("Three items in the middle of the list are:")
print(favorite_pizzas[1:4])

# • Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.
print("The last three items in the list are")
print(favorite_pizzas[-3:])

# Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
friend_pizzas = favorite_pizzas[:]

# Then, do the following:

# Add a new pizza to the original list.
favorite_pizzas.append('pesto')

# • Add a different pizza to the list friend_pizzas.
friend_pizzas.append('anchovy')

# • Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.
print("My favorite pizzas are:")
print(favorite_pizzas)
print("\n My friend's favorite pizzas are:")
print(friend_pizzas)

# All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

print("\nUsing a loop, here are my favorite pizzas:")

for pizza in favorite_pizzas[:]:
    print(pizza)

print("\nUsing a loop, here are my friend's favorite pizzas:")

for pizza in friend_pizzas[:]:
    print(pizza)



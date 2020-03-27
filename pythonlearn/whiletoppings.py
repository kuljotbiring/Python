# Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.
prompt_topping = "\nPlease enter the pizza topping you would like"
prompt_topping += "\nEnter 'quit to finish adding toppings: "

while True:
    topping = input(prompt_topping)

    if topping == 'quit':
        break

    print(f"Adding {topping} to your pizza")

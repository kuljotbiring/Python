# Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.


# Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python.

def make_shirt(size='large', message='I love Python'):
    print(f'The shirt made is size {size.title()} with "{message.upper()}" printed on it')


# Make a large shirt and a medium shirt with the default message, and a
# shirt of any size with a different message.
make_shirt('large')
make_shirt('medium')
make_shirt('small', 'buy this man a beer')

# Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.
print("\n")


def describe_city(city, country='north america'):
    print(f"{city.title()} is in {country.title()}")


describe_city('san francisco')
describe_city(city='venice', country='italy')
describe_city('tokyo', 'japan')

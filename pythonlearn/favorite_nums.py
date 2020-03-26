# Use a dictionary to store information about a person you know. Store their first name,
# last name, age, and the city in which they live. You should have keys such as first_name,
# last_name, age, and city. Print each piece of information stored in your dictionary

person = {
    'first_name': 'elon',
    'last_name': 'musk',
    'age': 45,
    'city': 'los angelos',
    }

print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())

# Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

favorite_numbers = {
    'mike': 12,
    'jerry': 23,
    'greg': 9,
    'kj': 7,
    'loyd': 40,
}
number = favorite_numbers['mike']
print(f"Mike's favorite number is: {number}")
number = favorite_numbers['jerry']
print(f"Jerry's favorite number is: {number}")
number = favorite_numbers['greg']
print(f"Greg's favorite number is: {number}")
number = favorite_numbers['kj']
print(f"KJ's favorite number is: {number}")
number = favorite_numbers['loyd']
print(f"Loyd's favorite number is: {number}")

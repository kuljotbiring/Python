# Start with the program you wrote for Exercise 6-1 (page 99).
tesla = {
    'first_name': 'elon',
    'last_name': 'musk',
    'age': 45,
    'city': 'los angeles',
    }

# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
microsoft = {
    'first_name': 'bill',
    'last_name': 'gates',
    'age': 70,
    'city': 'seattle',
    }

apple = {
    'first_name': 'steve',
    'last_name': 'jobs',
    'age': 63,
    'city': 'cupertino',
    }

ceo_list = []

ceo_list.append(tesla)
ceo_list.append(microsoft)
ceo_list.append(apple)

for founder in ceo_list:
        fullname = founder['first_name'].title() + " " + founder['last_name'].title()
        years = founder['age']
        location = founder['city'].title()

        print(f"{fullname} is {years} years old and lives in {location}")

# Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
major_rivers = {'egypt': 'nile', 'brazil': 'amazon', 'china': 'yangtze'}

# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
for key, value in major_rivers.items():
    print(f"\nThe {value.title()} river runs through {key.title()}")

# • Use a loop to print the name of each river included in the dictionary.
print("\nThe major rivers are:")
for value in major_rivers.values():
    print(value.title())
# • Use a loop to print the name of each country included in the dictionary.
print("\nThe countries the major world rivers are located in are:")
for key in major_rivers.keys():
    print(key.title())

# Use the code in favorite_languages.py (page 97).
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
voters = ['judy', 'jen', 'stacy', 'rick', 'frank', 'sarah', 'joe']

# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

for name in voters:
    if name not in favorite_languages.keys():
        print(f"{name.title()}, please take the poll ASAP")

    else:
        print(f"{name.title()}, thank you for taking the poll")
        

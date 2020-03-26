# Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person.
favorite_places = {
    'jennifer': ['japan', 'switzerland', 'australia'],
    'braxton': ['france', 'africa'],
    'katie': ['thailand']
}

# Loop through the dictionary, and print
# each person’s name and their favorite places.
for name, locations in favorite_places.items():
    print(f"{name.title()}'s favorite place(s):")

    for location in locations:
        print(f"\t{location.title()}")

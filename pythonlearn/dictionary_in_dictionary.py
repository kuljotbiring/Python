# Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact.

cities = {
    'vancouver': {
        'country': 'canada',
        'population': 675218,
        'language': 'french/english'
    },

    'new york': {
        'country': 'united states of america',
        'population': 8623000,
        'language': 'english'
    },

    'san francisco': {
        'country': 'united states of america',
        'population': 884363,
        'language': 'english'
    },
}

# Print the name of each city and all of the information
# you have stored about it.
for city, city_info in cities.items():
    print(f"\n city: {city.title()}")
    print(f"\t {city_info['country'].title()}")
    print(f"\t {city_info['population']}")
    print(f"\t {city_info['country'].title()}")


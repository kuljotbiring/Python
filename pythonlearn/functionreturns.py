# Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"


def make_album(city, country='north america'):
    return city.title() + ", " + country.title()


city_selection = make_album('vancouver', 'canada')

print(city_selection)


# Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.

def make_album(artist_name, album_title):
    music_album = {'Artist': artist_name.title(), 'Album': album_title.title()}
    return music_album


fav_album = make_album('metallica', 'enter sandman')
print(fav_album)

# Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

while True:
    print("\nPlease enter your favorite album artist and title:")
    print("Press 'q' to quit at any time")
    artist = input("Artist: ")

    if artist == 'q':
        break

    title = input("Title: ")

    if title == 'q':
        break

    best_album = make_album(artist, title)

    print(best_album)

# Make several dictionaries, where each dictionary represents a different
# pet. In each dictionary, include the kind of animal and the owner’s name.

canine = {
    'type': 'dog',
    'owner': 'Ralph'
}

cat = {
    'type': 'cat',
    'owner': 'betty'
}

equestrian = {
    'type': 'horse',
    'owner': 'john'
}

reptile = {
    'type': 'snake',
    'owner': 'sam'
}

rodent = {
    'type': 'gerbil',
    'owner': 'lisa'
}

# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pet_list = []
pet_list.append(canine)
pet_list.append(cat)
pet_list.append(equestrian)
pet_list.append(reptile)
pet_list.append(rodent)

for animal in pet_list:
    creature = animal['type']
    master = animal['owner'].title()

    print(f"{master} owns a {creature} as a pet")

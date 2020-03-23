# Think of at least five places in the world you’d like to
# visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.

travel_list = ['italy', 'greece', 'switzerland', 'japan', 'thailand', 'new zealand', 'brazil', 'peru', 'hong kong']

# • Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
print(travel_list)

# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
print(sorted(travel_list))

# • Show that your list is still in its original order by printing it again.
print(travel_list)

# • Use sorted() to print your list in reverse alphabetical order without changing
# the order of the original list.
print(sorted(travel_list, reverse=True))

# • Show that your list is still in its original order by printing it again.
print(travel_list)

# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
reversed(travel_list)

# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
reversed(travel_list)

# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
travel_list.sort()
print(travel_list)

# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.
travel_list.sort(reverse=True)
print(travel_list)




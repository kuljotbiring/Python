# If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

guest_list = ['superman', 'goku', 'thanos']

print(f"Dear {guest_list[0].title()}, I would like you cordially invite you to my dinner party - KJ")
print(f"Dear {guest_list[1].title()}, I would like you cordially invite you to my dinner party - KJ")
print(f"Dear {guest_list[2].title()}, I would like you cordially invite you to my dinner party - KJ")

# You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.

print(f"{guest_list[2].title()}, is unable to make it to the party")

guest_list[2] = 'magneto'

print(f"Dear {guest_list[0].title()}, I would like you cordially invite you to my dinner party - KJ")
print(f"Dear {guest_list[1].title()}, I would like you cordially invite you to my dinner party - KJ")
print(f"Dear {guest_list[2].title()}, I would like you cordially invite you to my dinner party - KJ")

# You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

print("A bigger table for the dinner has been found to accommodate more guests!")

guest_list.insert(0, 'professor x')
guest_list.insert(2, 'iron man')
guest_list.append('juggernaut')

print(f"Dear {guest_list[0].title()}, I would like you cordially invite you to my dinner party - KJ")
print(f"Dear {guest_list[1].title()}, I would like you cordially invite you to my dinner party - KJ")
print(f"Dear {guest_list[2].title()}, I would like you cordially invite you to my dinner party - KJ")
print(f"Dear {guest_list[3].title()}, I would like you cordially invite you to my dinner party - KJ")
print(f"Dear {guest_list[4].title()}, I would like you cordially invite you to my dinner party - KJ")
print(f"Dear {guest_list[5].title()}, I would like you cordially invite you to my dinner party - KJ")

# You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

print("Dear guests, I regret to inform you that I can only invite two people to dinner.")

removed_guest = guest_list.pop(0)
print(f"Dear, {removed_guest.title()}, you have been uninvited from the dinner")

removed_guest = guest_list.pop()
print(f"Dear, {removed_guest.title()}, you have been uninvited from the dinner")

removed_guest = guest_list.pop()
print(f"Dear, {removed_guest.title()}, you have been uninvited from the dinner")

removed_guest = guest_list.pop(1)
print(f"Dear, {removed_guest.title()}, you have been uninvited from the dinner")

del guest_list[1]
del guest_list[0]

print(guest_list)


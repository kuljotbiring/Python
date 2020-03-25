# Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:
# If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.

user_list = ['jake', 'mike', 'tom', 'jeff', 'larry', 'admin', 'scott']

# check for empty list
if user_list:
    for user in user_list:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?\n")

        else:
            print(f"Hello {user}, thank you for logging in again!\n")

else:
    print("\nWe need to find some users!")

# • Make a list of five or more usernames called current_users.
current_users = user_list[:5]

# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
new_users = current_users[-2:]
new_users.append('bruce')
new_users.append('nathan')
new_users.append('jerry')


# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
for user in new_users:
    if user in current_users:
        print(f"The username: {user} has already been taken. Enter a new username")

    else:
        print(f"The username {user} is available")




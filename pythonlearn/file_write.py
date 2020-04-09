# Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.

user_name = input("Please type your name and press enter: ")

name_file = 'guest.txt'

with open(name_file, 'w') as f:
    f.write(user_name)

while True:
    your_name = input("Please type your name to enter guest book or 'q' to quit: ")

    if your_name == 'q':
        break

    print(f"Hi {your_name}, thanks for signing in!")

    with open('guest_book.txt', 'a') as f:
        f.write(your_name + "\n")

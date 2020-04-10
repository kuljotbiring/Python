# One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number. Wrap your code in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.

while True:
    print("Please enter valid numbers when prompted and I'll add them. Or press q at anytime to quit")

    first_num = input("Enter the first number: ")

    if first_num == 'q':
        break

    else:
        try:
            first_num = int(first_num)

        except ValueError:
            print("Please enter a valid integer!")
            continue

    second_num = input("Enter the second number: ")

    if second_num == 'q':
        break

    else:
        try:
            second_num = int(second_num)

        except ValueError:
            print("Please enter a valid integer!")
            continue

    result = first_num + second_num

    print(f"{first_num} + {second_num} = {result}")


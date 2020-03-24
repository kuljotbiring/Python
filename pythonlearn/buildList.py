# Use a for loop to print the numbers from 1 to 20,
# inclusive.

for number in range(1, 21):
    print(number)

# Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

for number in range(1, 1_000_001):
    print(number)

# Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

million_numbers = []
for number in range(1, 1_000_001):
    million_numbers.append(number)

print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))

# Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

for number in range(3, 31, 3):
    print(number)

# A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

cube_nums = []

for number in range(1, 11):
    cubed = number ** 3
    cube_nums.append(cubed)

for cube in cube_nums:
    print(cube)

# Use a list comprehension to generate a list of the
# first 10 cubes.

cube_list = [number ** 3 for number in range(1, 11)]

for cube in cube_list:
    print(cube)

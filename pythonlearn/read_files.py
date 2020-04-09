# Open a blank file in your text editor and write a few
# lines summarizing what you’ve learned about Python so far. Start each line
# with the phrase In Python you can. . . . Save the file as learning_python.txt in
# the same directory as your exercises from this chapter. Write a program that
# reads the file and prints what you wrote three times.


# Print the contents once by
# reading in the entire file
with open('learning_python.txt') as file_object:
    data = file_object.read()

print(data)

# once by looping over the file object
with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.strip())

# and once by storing
# the lines in a list and then working with them outside the with block.

with open('learning_python.txt') as file_object:
    my_list = file_object.readlines()

for file_line in my_list:
    print(file_line.strip())

# Read in each line from the file you just created, learning_python.txt, and
# replace the word Python with the name of another language, such as C. Print
# each modified line to the screen.

with open('learning_python.txt') as file_object:
    my_list = file_object.readlines()

for file_line in my_list:
    file_line = file_line.strip()
    print(file_line.replace('Python', 'C'))

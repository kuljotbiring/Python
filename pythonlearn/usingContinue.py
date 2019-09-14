# uses continue which skips current iteration and moves to next iteration

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

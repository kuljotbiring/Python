# Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message. If the score is
# between 0.0 and 1.0, print a grade using the following table:
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

userGrade = input('Enter a score: ')

userGrade = float(userGrade)

if userGrade > 1.0 or userGrade < 0.0:
    print('Bad score')

elif userGrade >= .9:
    print('A')

elif floatuserGrade >= .8:
    print('B')

elif userGrade >= .7:
    print('C')

elif userGrade >= .6:
    print('D')

else:
    print('F')

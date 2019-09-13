# Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.
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


def compute_grade(grade):

    if userGrade > 1.0 or userGrade < 0.0:
        score = 'Bad score'

    elif userGrade >= .9:
        score = 'A'

    elif float(userGrade) >= .8:
        score = 'B'

    elif userGrade >= .7:
        score = 'C'

    elif userGrade >= .6:
        score = 'D'

    else:
        score = 'F'

    return score


your_grade = compute_grade(userGrade)

print(your_grade)

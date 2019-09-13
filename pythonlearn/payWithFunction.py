# Rewrite your pay computation with time-and-a-half for over-
# time and create a function called compute_pay which takes two parameters
# (hours and rate).

user_hours = input('Enter your hours worked: ')

user_hours = float(user_hours)

user_pay = input('Enter the rate per hour: ')

user_pay = float(user_pay)


def compute_pay(hours, rate):
    
    if user_hours > 40:
        over_time = user_hours - 40

        total_pay = (over_time * (user_pay * 1.5)) + (40 * user_pay)

        return total_pay

    else:
        total_pay = (user_hours * user_pay)
        
        return total_pay


total_comp = compute_pay(user_hours, user_pay)

print('Your total pay today is: ', total_comp)

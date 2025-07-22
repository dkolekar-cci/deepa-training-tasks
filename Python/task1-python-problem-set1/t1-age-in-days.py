# Task 1: Calculate Age in Days 

DAYS_IN_YEAR = 365

def calculate_age_in_days(age):
    return age * DAYS_IN_YEAR

try:
    age = int(input("Enter your age in years: "))
    if age < 0:
        print("Invalid input. Please enter a positive age.")
    else:
        total_days = calculate_age_in_days(age)
        print("You are", total_days, "days old.")
except ValueError:
    print("Invalid input. Please enter your age as a number.")
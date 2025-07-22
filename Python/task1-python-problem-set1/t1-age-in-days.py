# Task 1: Calculate Age in Days 

DAYS_IN_YEAR = 365

def calculate_age_in_days(age):
    if age < 0:
        return "Please enter a positive age."
    return age * DAYS_IN_YEAR


age = int(input("Enter your age in years: "))
    
total_days = calculate_age_in_days(age)
print("You are", total_days, "days old.")

total_days = calculate_age_in_days(-1)
print("You are", total_days, "days old.")

total_days = calculate_age_in_days(0)
print("You are", total_days, "days old.")




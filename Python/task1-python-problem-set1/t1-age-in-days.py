# Task 1: Calculate Age in Days 

def calculate_age_in_days(age, days_in_year):
    return age * days_in_year

age = int(input("Enter your age in years: "))
days_in_year = int(input("Enter number of days in a year: "))

total_days = calculate_age_in_days(age, days_in_year)

print("You are", total_days, "days old.")

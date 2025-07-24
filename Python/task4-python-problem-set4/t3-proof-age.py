import math
age_input = input("Enter your age: ")

try:
    age = float(age_input)  

    if age != math.floor(age):
        print("Please enter a whole number.")

    elif age <= 0:
        print("Age must be a positive number.")

    elif age > 120:
        print("Age must be between 1 and 120.")

    else:
        print("Age accepted.")
        
except:
    print("Invalid input. Please enter a numeric age.")
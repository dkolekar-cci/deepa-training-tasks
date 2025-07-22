# Task 4: Sum of Digits

def sum_of_digits(number):
    if number < 0:
        return "Invalid Input! Please enter a positive number."
    
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10
    return total

user_input = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(user_input))

# hardcoded call
print("Sum of digits:", sum_of_digits(123))
print("Sum of digits:", sum_of_digits(428))
print("Sum of digits:", sum_of_digits(0))
print("Sum of digits:", sum_of_digits(-1))


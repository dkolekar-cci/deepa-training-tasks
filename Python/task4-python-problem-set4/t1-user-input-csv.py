import csv
import string

def valid_name(name):
    for char in name:
        if char not in string.ascii_letters:
            return False
    return True

def valid_email(email):
    return "@" in email and "." in email

def save_to_csv(user_data):
    try:
        with open("users.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(user_data)
            print("User saved to users.csv")
    except IOError:
        print("Error saving to file.")

def get_user_input():
    try:
        name = input("Enter your name: ")
        if not valid_name(name):
            print("Invalid name. Use alphabet letters only.")
            return

        age_input = input("Enter your age: ")
        if not age_input.isdigit():
            print("Invalid age. Use numbers only.")
            return
        age = int(age_input)

        email = input("Enter your email: ")
        if not valid_email(email):
            print("Invalid email. Must contain @ and .")
            return

        save_to_csv([name, age, email])
    
    except Exception as e:
        print("An error occurred:", e)
        
get_user_input()
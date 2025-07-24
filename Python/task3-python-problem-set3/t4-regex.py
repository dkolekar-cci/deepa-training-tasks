import re

class Validator:
    def __init__(self, input_data):
        self.input = input_data

    def email(self):
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}$'
        return re.match(pattern, self.input) is not None

    def phone(self):
        pattern = r'^[789]\d{9}$'
        return re.match(pattern, self.input) is not None

    def classify(self):
        if self.email():
            return "Valid Email"
        elif self.phone():
            return "Valid Phone Number"
        else:
            return "Invalid Input"

user_input = input("Enter email or phone number: ")
print(Validator(user_input).classify())
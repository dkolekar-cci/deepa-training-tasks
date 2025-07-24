import re

input = "Hi, I am dee572@gmail.com, Please contact at support@mywebsite.com, hr@company.org, or feedback123@test.co.in for more info."
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'

emails = re.findall(pattern, Input)

print("Emails found:", emails)
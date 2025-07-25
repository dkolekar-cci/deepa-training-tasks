import json

def read_students_from_file():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
            return data
    except:
        print("Could not read file.")
        return []

def format_student_output(student):
    return student["name"] + "- " + str(student["marks"]) + " marks"

def main():
    students = read_students_from_file()
    for student in students:
        result = format_student_output(student)
        print(result)

main()
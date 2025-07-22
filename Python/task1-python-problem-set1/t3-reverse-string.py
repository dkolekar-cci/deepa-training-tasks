# Task 3: Reversing a String 

def Reverse_String(text):
    reversed_text = ""  
    for char in text:   
        reversed_text = char + reversed_text  
    return reversed_text

input_string = input("Enter a string to reverse: ")

print("Reversed string:", Reverse_String(input_string))


#hardcoded values
print("Reversed string:", Reverse_String("hello"))
print("Reversed string:", Reverse_String("goa"))
print("Reversed string:", Reverse_String("India"))

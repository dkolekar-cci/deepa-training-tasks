#Task 8: Sentence value

def sentence_value(sentence_input):
    sentence = sentence_input.lower()
    total_value = 0

    for char in sentence:
        if 'a' <= char <= 'z':
            value = ord(char) - ord('a') + 11
            total_value += value

    return total_value

user_input = input("Enter a sentence: ")
print("value of " + user_input + " is " + str(sentence_value(user_input)))

# Hardcoded calls
print("value of 'Test' is " + str(sentence_value("Test")))
print("value of 'Hello World' is " + str(sentence_value("Hello World")))
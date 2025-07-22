import string

paragraph = input("Enter a paragraph: ")

for symbol in string.punctuation:
    paragraph = paragraph.replace(symbol, "")

paragraph = paragraph.lower()

words = paragraph.split()

unique_words = set(words)

sorted_words = sorted(unique_words)

print("Unique words:", sorted_words)

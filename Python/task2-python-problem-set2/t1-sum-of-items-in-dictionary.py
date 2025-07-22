#Task 1: Sum of all items in a dictionary

def Sum_of_Items(dict_input):
    total = 0
    for key in dict_input:
        total = total + dict_input[key]
    return total

print(Sum_of_Items({'a': 400, 'b': 200, 'c': 300}))  
print(Sum_of_Items({'x': 35, 'y': 18, 'z': 45}))     
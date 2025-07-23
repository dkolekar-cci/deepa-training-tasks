def check_number_in_arrays(num):
    array_one = [1, 5, 8, 9, 10]
    array_two = [5, 8, 9, 10, 12, 20, 40, 60, 70]

    found_in_array_one = num in array_one
    found_in_array_two = num in array_two

    if found_in_array_one and found_in_array_two:
        return f"number {num} found in both arrays"
    elif found_in_array_one:
        return f"number {num} found in array_one"
    elif found_in_array_two:
        return f"number {num} found in array_two"
    else:
        return f"number {num} not found in any array"

input_number = int(input("Enter the number to search: "))
print(check_number_in_arrays(input_number))

#hardcoded calls
print(check_number_in_arrays(9))
print(check_number_in_arrays(70))
print(check_number_in_arrays(100))

def find_indices(num_list, target):
    dictionary = {}

    for current_index, current_number in enumerate(num_list):
        difference = target - current_number

        if difference in dictionary:
            return [dictionary[difference], current_index]
        dictionary[current_number] = current_index

print(find_indices([2, 7, 11, 15], 9))
print(find_indices([3, 2, 4], 6))
print(find_indices([3, 3], 6))

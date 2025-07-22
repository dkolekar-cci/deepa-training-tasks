def Swap_first_last(list):
    
    temp = list[0]

    list[0] = list[len(list) - 1]

    list[len(list) - 1] = temp

    return list

print(Swap_first_last([12, 35, 9, 56, 24]))  
print(Swap_first_last([1, 2, 3]))            
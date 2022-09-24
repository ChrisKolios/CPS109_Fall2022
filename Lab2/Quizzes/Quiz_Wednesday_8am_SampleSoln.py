def We8_SSF(my_list, my_scalar):
    for i in range(len(my_list)):
        if (my_list[i] != 4):
            my_list[i] = my_list[i] * my_scalar
    return my_list

def We8_SSBF(my_list, my_scalar): # Bonus
    duplicates = []
    for i in range(len(my_list)):
        if (my_list[i] not in duplicates):
            duplicates.append(my_list[i])
            if (my_list[i] != 4):
                my_list[i] = my_list[i] * my_scalar
        else:
            return -1
    return my_list

if __name__ == "__main__":
    my_input_list = []
    num_ints = int(input("How many numbers in list: "))
    for i in range(num_ints):
        my_input_list.append(int(input()))
    scalar_value = int(input("Enter scalar value: "))
    print(We8_SSF(my_input_list, scalar_value))

    my_input_list = [] # Bonus
    num_ints = int(input("How many numbers in list: "))
    for i in range(num_ints):
        my_input_list.append(int(input()))
    scalar_value = int(input("Enter scalar value: "))
    print(We8_SSBF(my_input_list, scalar_value))

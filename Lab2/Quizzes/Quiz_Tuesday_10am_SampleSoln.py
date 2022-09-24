def Tu10_SSF(my_list):
    full_operation = 0
    for i in range(len(my_list)):
        if (i % 2 == 0): # Even
            full_operation += my_list[i]
        else:
            full_operation -= my_list[i]
    return full_operation

def Tu10_SSBF(my_list):
    full_operation = 0
    numbers_seen_before = []
    for i in range(len(my_list)):
        if my_list[i] not in numbers_seen_before:
            numbers_seen_before.append(my_list[i])
            if (i % 2 == 0): # Even
                full_operation += my_list[i]
            else:
                full_operation -= my_list[i]
        else:
            return full_operation
    return full_operation

if __name__ == "__main__":
    my_input_list = []
    num_ints = int(input())
    for i in range(num_ints):
        my_input_list.append(int(input()))
    print(Tu10_SSF(my_input_list))

    my_input_list = []
    num_ints = int(input())
    for i in range(num_ints):
        my_input_list.append(int(input()))
    print(Tu10_SSBF(my_input_list))

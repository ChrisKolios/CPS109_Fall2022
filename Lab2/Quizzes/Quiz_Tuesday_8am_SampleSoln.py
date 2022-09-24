def Tu8_SSF(my_list):
    for i in range(len(my_list)):
        if (i % 2 == 0): # Even
            print(my_list[i] + "?")
        else:
            print(my_list[i] + "!")

def Tu8_SSBF(my_list):
    for i in range(len(my_list)):
        my_list[i] = my_list[i].replace("r", "w")
        my_list[i] = my_list[i].replace("l", "w")
        if (i % 2 == 0): # Even
            print(my_list[i] + "?")
        else:
            print(my_list[i] + "!")

if __name__ == "__main__":
    my_input_list = []
    num_strings = int(input())
    for i in range(num_strings):
        my_input_list.append(input())
    Tu8_SSF(my_input_list)

    my_input_list = []
    num_strings = int(input())
    for i in range(num_strings):
        my_input_list.append(input())
    Tu8_SSBF(my_input_list)

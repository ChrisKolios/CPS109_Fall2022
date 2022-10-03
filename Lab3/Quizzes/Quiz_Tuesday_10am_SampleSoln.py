def Tu10_SSF(my_list):
    guarded_list = []
    for i in range(len(my_list)):
        guarded_list.append(my_list[i]) # We always append...
        if (i != len(my_list)-1): # If we are not at the last element...
            if (abs(my_list[i] - my_list[i+1]) == 1): # If 1 < / >
                guarded_list.append("GUARD")
    return guarded_list
            
def Tu10_SSBF(my_list):
    pass # No bonus today...

if __name__ == "__main__":
    my_input_list = []
    num_ints = int(input("Enter the number of integers in your list: "))
    while (len(my_input_list) < num_ints):
        temp_input = int(input("Enter a non-zero number: "))
        if (temp_input != 0):
            my_input_list.append(temp_input)
        else:
            print("Hey! I said you can't enter 0! >:(")
    print(Tu10_SSF(my_input_list))

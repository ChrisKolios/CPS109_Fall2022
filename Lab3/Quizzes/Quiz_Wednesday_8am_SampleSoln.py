def We8_SSF(my_list):
    e_pruned_list = [] # What we will eventually return
    for string_element in my_list: # For each string in the list...
        str_to_add = "" # Creating some empty string to add to...
        num_e_counter = 0 # For each string, assume 0 e's to start
        for j in range(len(string_element)): # For each character in the list element
            if (string_element[j] == "e"):
                num_e_counter += 1
            else:
                str_to_add += string_element[j]
        if (num_e_counter < 5): # If less than 5 individual e's in the string...
            e_pruned_list.append(str_to_add) # Add that string (with pruned e's) to our output list
        # Otherwise we do nothing (as we don't want to add that list)
    return e_pruned_list
            
def We8_SSBF(my_list):
    pass # No bonus today...

if __name__ == "__main__":
    my_input_list = []
    num_strings = int(input("Enter the number of strings in your list: "))
    while (len(my_input_list) < num_strings): # We use a while loop here to ensure num_strings elements are added
        temp_input = input("Enter a string to add to your list: ")
        if (temp_input != "sneak"): # If they don't enter the forbidden string "sneak"
            my_input_list.append(temp_input) # Then we can add their input to the list
        else: # Otherwise
            print('Nice try, but no "sneak"ing in my list!') # Chide them
    print(We8_SSF(my_input_list))

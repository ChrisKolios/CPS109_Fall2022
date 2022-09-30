def Fr8_SSF(my_list): # We define a function Friday 8am Sample Solution Function (which takes in some list as input)
    my_new_list = [] # We start by creating some empty new list to add things to
    for i in range(len(my_list)): # We iterate over all elements in the list...
        temp_str = my_list[i] # We set some string temp_str to equal the string at that location in the list
        num_t = 0 # Critically, we notice we have our counters only within the FIRST loop. It is not nested, because for each
        num_c = 0 # new character we need to reset our t and c counters!
        for character in temp_str: # For each character in the string...
            if (character == "t"): # If we encounter a t...
                num_t += 1 # Increment the t counter
            elif (character == "c"): # If we encounter a c...
                num_c += 1 # Increment the c counter
        if not((num_t > 3) or (num_c < 4)): # If the number of t's is <= 3 and the number of c's >= 4 (i.e. valid string)
        # Equivalently written: if (num_t <= 3 and num_c >= 4)
            my_new_list.append(temp_str) # Then add the string to the list
    return my_new_list # Return the string

def Fr8_SSBF(my_list): # Bonus
    my_new_list = []
    for i in range(len(my_list)):
        temp_str = my_list[i]
        num_t = 0
        num_c = 0
        for character in temp_str:
            if (character == "t"):
                num_t += 1
            elif (character == "c"):
                num_c += 1
        if not((num_t > 3) or (num_c < 4)):
        # Equivalently written: if (num_t <= 3 and num_c >= 4)
            partially_uwuified_string_element = temp_str.replace("r", "w") # uwu
            uwuified_string_element = partially_uwuified_string_element.replace("l", "w")
            my_new_list.append(uwuified_string_element)
    return my_new_list

if __name__ == "__main__": # Remember, everything should be in a function or in the if __name__ == "__main__"!
    my_input_list = [] # Create some new empty list for user input
    num_strings = int(input("How many strings in list: ")) # Get user input and cast to an int
    for i in range(num_strings): # Iterate num_strings times...
        my_input_list.append(input()) # And prompt the user for a string, adding it to the list
    print(Fr8_SSF(my_input_list)) # Run the function

    my_input_list = [] # Bonus
    num_strings = int(input("How many strings in list: "))
    for i in range(num_strings):
        my_input_list.append(input())
    print(Fr8_SSBF(my_input_list))

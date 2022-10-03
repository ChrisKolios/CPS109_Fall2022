def Thurs10_SSF(my_list):
    max_t_string = None # Start with nothing
    max_t_count = 0
    for string_element in my_list:
        t_count = 0
        for character in string_element:
            if (character == "t"):
                t_count += 1
        if (t_count >= max_t_count):
            max_t_count = t_count
            max_t_string = string_element
    print(max_t_count)
    return max_t_string   
            
def Thurs10_SSBF(my_list):
    pass # No bonus today...

if __name__ == "__main__":
    my_input_list = []
    num_strings = int(input("Enter the number of strings in your list: "))
    while (len(my_input_list) < num_strings): # We use a while loop here to ensure num_strings elements are added
        temp_input = input("Enter a string: ")
        # We can use temp_input.contains("c") or "c" in temp_input, but we can also just use a for loop and check ourselves
        c_in_input = False
        for character_value in temp_input:
            if (character_value == "c"):
                c_in_input = True
                break # Break out of the loop (for efficiency - though we don't have to do this)
        if (c_in_input == False): # If valid input...
            my_input_list.append(temp_input) # Then we can add their input to the list
        else: # Otherwise
            print("Hey! I said no 'c's!") # Let them know it was wrong
    print(Thurs10_SSF(my_input_list))

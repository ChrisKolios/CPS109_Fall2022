def Tu8_SSF(my_list, magicnum):
    good_vals_list = []
    tpi = 0 # True position index
    for i in range(len(my_list)):
        #print("i", i, "tpi", tpi, "my_list[i]", my_list[i])
        if (tpi != magicnum and my_list[i] == tpi): # Then remove
            continue # Here we don't actually remove - instead we
            # just don't add it to the list of good values
            # Notice that we don't update our true position index
            # This is because our output list is "stuck" at this index
            # until it encounters a suitable value
        else: # If the value is fine to add...
            good_vals_list.append(my_list[i]) # Add it to our new list
            tpi += 1 # And now consider the following index in our new list
    return good_vals_list

def Tu8_SSAF(my_list, magicnum): # Alternate way of writing...
    good_vals_list = []
    tpi = 0
    for i in range(len(my_list)):
        if not (tpi != magicnum and my_list[i] == tpi): #a.k.a. if tpi == magicnum or my_list[i] != tpi...
            good_vals_list.append(my_list[i])
            tpi += 1
    return good_vals_list

def Tu8_SSAF2(my_list, magicnum): # Alternate way of writing (while loop)
    current_index = 0
    good_vals_list = []
    while(my_list): # I.e. while len(my_list > 0):
        temp_val = my_list.pop(0) # Remove the first element
        if (current_index == magicnum or temp_val != current_index):
            good_vals_list.append(temp_val)
            current_index += 1
    return good_vals_list

def Tu10_SSBF(my_list):
    pass # No bonus today...

if __name__ == "__main__":
    my_input_list = [0, 1, 1, 3, 2, 4, 4, 4, 5]
    magicnum = int(input("Enter the magic number: "))
    print(Tu8_SSF(my_input_list, magicnum)) # Normal solution
    print(Tu8_SSAF(my_input_list, magicnum)) # Simplified solution
    print(Tu8_SSAF2(my_input_list, magicnum)) # While loop solution
    

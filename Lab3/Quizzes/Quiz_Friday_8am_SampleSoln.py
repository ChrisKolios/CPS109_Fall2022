def Fri8_SSF(my_list): 
    letter_list = [""] * len(my_list) # Again, we could use a for loop here.
    sum_list = [0] * len(my_list) # We could also use a for loop here, or not even set to 0 yet. This just avoids appends.
    for i in range(len(my_list)):
        for temp_char in my_list[i]: # Iterating by element here...
            if (temp_char.isdigit() == True):
                sum_list[i] += int(temp_char) # This shouldn't give an error as we verity it is a digit beforehand
                # In this approach we directly add it to the sum list
            else: # If not a number...
                letter_list[i] += temp_char
    return letter_list, sum_list # Can just as easily put this into a list if desired...
            
def Fri8_SSFA(my_list): # An alternate approach to this problem, doing things a bit more naively perhaps
    letter_list = []
    sum_list = [] # This time we don't prepopulate our list
    for i in range(len(my_list)):
        tempsum = 0
        tempstr = ""
        for temp_char in my_list[i]:
            if (temp_char.isdigit() == True): # Don't forget the brackets after .isdigit() here...
                tempsum += int(temp_char) # Again, here we directly sum. See SSFA2 for how to not directly sum.
            else:
                tempstr += temp_char
        # Now that we've created a temporary sum and temporary list, we can add it to the output lists
        letter_list.append(tempstr)
        sum_list.append(tempsum)
    return letter_list, sum_list

def Fri8_SSFA2(my_list): # Approach when not summing immediately (not recommended)
    letter_list = []
    sum_list = []
    for i in range(len(my_list)):
        inner_sum_list = [] # Create some inner sum list
        tempstr = ""
        for temp_char in my_list[i]:
            if (temp_char.isdigit() == True):
                inner_sum_list.append(int(temp_char))
            else:
                tempstr += temp_char
        letter_list.append(tempstr)
        sum_list.append(inner_sum_list) # 2D list... Hence why not recommended
        
    # Now we calculate the sum
    for i in range(len(sum_list)):
        total_sum = 0
        for number in sum_list[i]:
            total_sum += number
        sum_list[i] = total_sum
    return letter_list, sum_list
        
def Fri8_SSBF(my_list):
    pass # No bonus today...

if __name__ == "__main__":
    my_input_list = []
    num_strings = int(input("Enter the number of strings in your list: "))
    while (len(my_input_list) < num_strings): # We use a while loop here to ensure num_strings elements are added
        temp_input = input("Enter a string: ")
        # We can use temp_input.contains(".") or "." in temp_input, but we can also just use a for loop and check ourselves
        period_in_input = False
        for character_value in temp_input:
            if (character_value == "."):
                period_in_input = True
                break # Break out of the loop (for efficiency - though we don't have to do this)
        if (period_in_input == False): # If valid input...
            my_input_list.append(temp_input) # Then we can add their input to the list
        else: # Otherwise
            print("Hey! I said no dots! Period!") # Let them know it was wrong 
    print(Fri8_SSF(my_input_list)) # All 3 approaches give the same answer...
    print(Fri8_SSFA(my_input_list))
    print(Fri8_SSFA2(my_input_list))

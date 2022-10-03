def Thurs8_SSF(my_list):
    for i in range(len(my_list)):
        digit_in_password = False
        h_counter = 0
        for character in my_list[i]:
            if (character.isdigit()): # If any character is a number...
                digit_in_password = True # Then we've seen a digit in this password
            elif (character == "h"):
                h_counter += 1
        # Now that we have gone through the whole password, check for if there is a digit
        if (digit_in_password == False): # If so, do nothing, but if not...
            my_list[i] += "1"
        if (h_counter < 3): # If we have less than 3 "h"s
            num_of_h_to_add = 3 - h_counter # Then we must have at least 3 "h"s, so calculate the difference
            my_list[i] += "h"*num_of_h_to_add # Then add the corresponding number of "h"s to the list
        if (len(my_list[i]) <= 4): # We calculate the length here, after having added numbers/"h"s if needed...
            num_of_h_to_add = 5 - len(my_list[i]) # Then we must have at least this many more characters
            my_list[i] += "h"*num_of_h_to_add # So add that many more "h"s
    return my_list
            
            
def Thurs8_SSBF(my_list):
    pass # No bonus today...

if __name__ == "__main__":
    my_input_list = []
    num_passwords = int(input("Enter the number of passwords in your list: "))
    while (len(my_input_list) < num_passwords): # We use a while loop here to ensure num_passwords elements are added
        temp_input = input("Enter a password: ")
        # We can use temp_input.contains("@") or "@" in temp_input, but we can also just use a for loop and check ourselves
        at_in_input = False
        for character_value in temp_input:
            if (character_value == "@"):
                at_in_input = True
                break # Break out of the loop (for efficiency - though we don't have to do this)
        if (at_in_input == False): # If valid input...
            my_input_list.append(temp_input) # Then we can add their input to the list
        else: # Otherwise
            print("The '@' symbol is reserved for emails! Please enter another password.") # Let them know it was wrong
    print(Thurs8_SSF(my_input_list))

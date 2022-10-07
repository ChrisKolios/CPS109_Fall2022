def missing_letters(termination_word):

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # print(len(alphabet)) # Sanity check for me cause I typed the above manually (lol)

    input_list = [] # Start with empty input list
    inp = "temp" # Start with a temporary value so that we enter the while loop

    while inp != termination_word: # While we don't terminate yet...
        inp = input("Enter a string: ") # Grab user input
        if (inp != termination_word):
            input_list.append(inp) # Add it to the list if it's not our termination word

    # We now have our completed list of user inputs

    output_list = [] # The list to output

    for i in range(len(input_list)):
        missing_letter_list = [] # Done on a per-string basis
        for letter in alphabet:
            if letter not in input_list[i]: # If the letter is not in the string...
                missing_letter_list.append(letter)
        # By the end of the loop, all non-present letters will be in missing_letter_list
        output_list.append(missing_letter_list)

    return output_list, input_list # Notice how we structure our return

if __name__ == "__main__":
    termination_word = "halt!" # Or whatever you want it to be...
    output_list, input_list = missing_letters(termination_word) # Notice how we grab our values and how we return them

    for i in range(len(input_list)):
        print(input_list[i] + " :", output_list[i]) # We iterate over all input strings and print their corresponding missing letter list

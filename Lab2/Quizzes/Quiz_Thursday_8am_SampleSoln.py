def Th8_SSF(my_list):
    num_vowels = 0
    for string_element in my_list:
        for ce in string_element: # Character element
            if (ce == "a" or ce == "e" or ce == "i" or ce == "o" or ce == "u"):
                num_vowels += 1
        if (string_element[-1] == "y"): # Notice we only have to check for y at the end of the string
            # This is just by an assumption in the problem statement. It might actually be
            # tricky to test if it occurs at the end of a word!
            num_vowels += 1
    return num_vowels

def Th8_SSBF(my_list): # Bonus
    num_vowels = 0
    my_uwuified_list = []
    for string_element in my_list:
        partially_uwuified_string_element = string_element.replace("r", "w")
        uwuified_string_element = partially_uwuified_string_element.replace("l", "w")
        my_uwuified_list.append(uwuified_string_element)
        word_list = string_element.split() # by default splits by whitespace
        for word in word_list:
            for ce in word: # Character element
                if (ce == "a" or ce == "e" or ce == "i" or ce == "o" or ce == "u"):
                    num_vowels += 1
            if (word[-1] == "y"): # Notice we only have to check for y at the end of the word
                # Again, this is by relaxed assumptions in the problem statement (consider punctuation!)
                num_vowels += 1
    return num_vowels, my_uwuified_list # We could equivalently return [num_vowels, my_uwuified_list]

if __name__ == "__main__":
    my_input_list = []
    num_strings = int(input("How many strings in list: "))
    for i in range(num_strings):
        my_input_list.append(input())
    print(Th8_SSF(my_input_list))

    my_input_list = [] # Bonus
    num_strings = int(input("How many strings in list: "))
    for i in range(num_strings):
        my_input_list.append(input())
    bonus_output = Th8_SSBF(my_input_list)
    print(bonus_output[0])
    print(bonus_output[1])

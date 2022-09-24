def Th10_SSF(my_list):
    reversed_list = []
    for i in range(len(my_list)):
        reversed_word = ''
        in_word = my_list[len(my_list)-i-1]
        for j in range(len(in_word)):
            reversed_word += in_word[len(in_word)-j-1]
        reversed_list.append(reversed_word)
        print(reversed_word)
    return reversed_list

def Th10_SSBF(my_list): # Bonus
    reversed_list = []
    for i in range(len(my_list)):
        reversed_word = ''
        in_word = my_list[len(my_list)-i-1]
        for j in range(len(in_word)):
            reversed_word += in_word[len(in_word)-j-1]
        partially_uwuified_string_element = reversed_word.replace("r", "w")
        uwuified_string_element = partially_uwuified_string_element.replace("l", "w")
        reversed_list.append(uwuified_string_element)
        print(uwuified_string_element)
    return reversed_list

if __name__ == "__main__":
    my_input_list = []
    num_strings = int(input("How many strings in list: "))
    for i in range(num_strings):
        my_input_list.append(input())
    print(Th10_SSF(my_input_list))

    my_input_list = [] # Bonus
    num_strings = int(input("How many strings in list: "))
    for i in range(num_strings):
        my_input_list.append(input())
    print(Th10_SSBF(my_input_list))

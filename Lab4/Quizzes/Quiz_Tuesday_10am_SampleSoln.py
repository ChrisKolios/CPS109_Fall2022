def Tu10_SampleSoln_Func1(): 
    final_clothes_list = [] # An empty list to start
    valid_colours = ["yellow", "orange", "red", "purple", "blue", "green"] # A list of all valid colours
    valid_articles = ["shirt", "pants", "dress", "sweater"] # A list of all valid articles
    # We can use these alongside the keyword "in" to simplify our input checking

    enter_colour_next = True # Just a boolean to track if a valid colour has yet to be entered
    temp_str = "" # Start with an empty temp string
    inp = "" # Just to start things off...
    while inp != "stop": # While not stop...
        if (enter_colour_next): # If they must enter a colour next
            inp = input("Enter a colour: ") # Grab some colour input
            if (inp in valid_colours): # If it is a valid colour
                temp_str += inp # Add the colour to our temp string
                enter_colour_next = False # Note that they should enter an article next
            else: # If not a valid colour
                print("Please enter a valid colour") # Print for the user to enter a valid colour
        else: # If not to enter a colour next (i.e. if to enter article next...)
            inp = input("Enter an article of clothing: ") # Grab some article input
            if (inp in valid_articles): # If it is a valid article
                temp_str += " " + inp # Add a space plus the article to our temp string
                final_clothes_list.append(temp_str) # Add that temp string to the input list
                temp_str = "" # Reset the temp string
                enter_colour_next = True # Note that they should enter a colour next
            else: # If not a valid article...
                print("Please enter a valid article of clothing") # Print for the user to enter a valid article
    return final_clothes_list # Return the clothes list at the end

def naive_helper_colour_function(colour): # Naive helper function for colour wheel
    if (colour == "yellow"):
        return "purple"
    if (colour == "orange"):
        return "blue"
    if (colour == "red"):
        return "green"
    if (colour == "purple"):
        return "yellow"
    if (colour == "blue"):
        return "orange"
    if (colour == "green"):
        return "red"

def better_helper_colour_function(colour): # Looks cooler
    colour_list = ["yellow", "orange", "red", "purple", "blue", "green"]
    return colour_list[-1 * (colour_list.index(colour) + 1)]

def Tu10_SampleSoln_Func2(clothes_list):
    colours_list = [] # We can create lists to represent just colours / just articles, but maintain indices
    articles_list = []

    for i in range(len(clothes_list)):
        colour = clothes_list[i].split(' ')[0]
        article = clothes_list[i].split(' ')[1] # We are wasting resources by calling split twice.
        # More efficient:
        # colour, article = clothes_list[i].split(' ')
        colours_list.append(colour)
        articles_list.append(article)

    # We can use a nested for loop here to check all possible combinations
    for i in range(len(colours_list)):
        for j in range(len(colours_list)):
            if (colours_list[i] == naive_helper_colour_function(colours_list[j])): # If the colours are complementary...
                if (articles_list[i] != articles_list[j]): # If they are not the same type of clothing...
                    print("Nice fit") # Then we have a valid pair so we print so...
                    return -1 # And just exit the loop
    print("Zero drip") # Otherwise if we've tested all combinations and there are no valid pairs we print so...
    return -1 # And just exit the loop

def Tu10_SSBF(my_list):
    pass # No bonus today...

if __name__ == "__main__":
    print(Tu10_SampleSoln_Func1())
    test_input1 = ["blue pants", "red dress", "orange sweater"]
    test_input2 = ["green pants", "purple dress", "blue shirt"]
    test_input3 = ["green shirt", "red shirt", "yellow pants"]
    Tu10_SampleSoln_Func2(test_input1)
    Tu10_SampleSoln_Func2(test_input2)
    Tu10_SampleSoln_Func2(test_input3)

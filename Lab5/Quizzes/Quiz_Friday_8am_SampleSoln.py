def Snacktorial(input_float):
    if (input_float <= 0): # Base Case 1 (negative or 0 input)
        return 0
    elif (input_float <= 1): # Base Case 2 (0 < input <= 1) 
        return input_float # Note that we need the <= (can't just be <)
    else: # Recursive Call
        return input_float * Snacktorial(input_float-1) # Input * Snacktorial(Input-1)

if __name__ == "__main__":
    my_input = float(input("Enter the number you'd like the Snacktorial of: "))
    print(Snacktorial(my_input))

def RecursiveAndOrFlip(bool_list):
    if (len(bool_list) == 0): # Base Case 1 (empty list)
        return False
    elif (len(bool_list) == 1): # Base Case 2 (1 item)
        return not bool_list[0] # Flips the value
    else: # Recursive Call
        odd_adder = len(bool_list)%2 # Either 0 if even or 1 if odd num of elements
        first_half = RecursiveAndOrFlip(bool_list[:len(bool_list)//2 + odd_adder]) # These recursive calls happen regardless of odd/even
        second_half = RecursiveAndOrFlip(bool_list[len(bool_list)//2 + odd_adder:]) # Notice that we split the list using indexing
        if (odd_adder == 1): # Odd
            #print(bool_list, ":", first_half, "and", second_half, "=", first_half and second_half) # Uncomment if you want to trace recursive calls
            return first_half and second_half # In the Odd case we use "and"
        else: # Even
            #print(bool_list, ":", first_half, "or", second_half, "=", first_half or second_half) # Uncomment if you want to trace recursive calls
            return first_half or second_half # In the Even case we use "or"

if __name__ == "__main__":
    bool_list = [True, False]
    print(RecursiveAndOrFlip(bool_list))
    bool_list = [True, False, False]
    print(RecursiveAndOrFlip(bool_list))
    bool_list = [False, False, True, False, True, True, False, True, True]
    print(RecursiveAndOrFlip(bool_list))

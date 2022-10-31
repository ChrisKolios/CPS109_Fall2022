def OddBonanza(list_to_bonanzafy):
    #print(list_to_bonanzafy) # Uncomment if you want to trace the recursive calls
    if (len(list_to_bonanzafy) == 0): # Base Case 1: Nothing in list
        return 0
    elif (len(list_to_bonanzafy) == 1): # Base Case 2: 1 integer in list
        last_num = str(list_to_bonanzafy[0])[-1] # Gets the last digit by first casting to a string
        if (last_num == "1"):
            return 9
        elif (last_num == "3"):
            return 7
        elif (last_num == "5"):
            return 5
        elif (last_num == "7"):
            return 3
        else: # last_num == 9 (we assume list of odd integers)
            return 1
    else: # Recursive Call: > 1 integer in list
        odd_adder = len(list_to_bonanzafy)%2 # Either 0 if even or 1 if odd num of elements (technically this does not matter, as we're just multiplying so order of operations is not important)
        first_half = OddBonanza(list_to_bonanzafy[:len(list_to_bonanzafy)//2 + odd_adder])
        second_half = OddBonanza(list_to_bonanzafy[len(list_to_bonanzafy)//2 + odd_adder:])
        #print(first_half, second_half, first_half*second_half) # Uncomment if you want to trace recursive calls
        return first_half * second_half 
        # Return the product of the OddBonanza of the first half and the OddBonanza of the second half

if __name__ == "__main__":
    list_to_bonanzafy = [1, 3, 5]
    print(OddBonanza(list_to_bonanzafy))
    list_to_bonanzafy = [31, 243, 1255]
    print(OddBonanza(list_to_bonanzafy))
    list_to_bonanzafy = [1, 3, 5, 7, 9]
    print(OddBonanza(list_to_bonanzafy))
    list_to_bonanzafy = [1, 9, 25, 49, 81, 905]
    print(OddBonanza(list_to_bonanzafy))

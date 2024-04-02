#Quiz Sample Solution
def text_decoder(text_to_read, secret_indices):
    decoder_dict = {} # Start with some empty dictionary
    message = '' # Start with some empty message string

    with open(text_to_read, 'r', encoding='utf8') as f: # Given the encoding part
        #f.tell() # We start from 0
        f.seek(2825) # Given (specific value for A Tale of Two Cities (from the start of the first chapter))
        file_str = f.read() # Read in the whole text
        file_lst = file_str.split() # And split it into individual words

        '''for i in secret_indices: # Iterate over all secret_indices
            if i == -1:
                message += '\n'
            else:
                if i not in decoder_dict: # If we have not already discovered the word associated with the index i
                    decoder_dict[i] = file_lst[i] # Set the dictionary key:value pair to index:word
                message += decoder_dict[i] + " " # Then access the dictionary to write the message''' # This is the way I'd do this

        for i in secret_indices: # How we instructed it to be done
            if i not in decoder_dict:
                decoder_dict[i] = file_lst[i]

        for i in secret_indices: # Note that the dictionary serves no efficiency purpose - we just wanted to make sure you know how to use them
            if i == -1:
                message += "\n"
            else:
                message += decoder_dict[i] + " "

    return decoder_dict, message # Return both the filled out dictionary as well as the message

if __name__ == '__main__':
    print("Starting decoding")

    secret_indices = [64, 1162, 561, 6801, 79, 14636, -1, 1670, 2300, 6, 31868, 130, 93, 413, 1663, -1, 124, 9991, 61592, 436, 1413, 1663, 2553, 51544, 8, -1, 1670, 1791, 406, 1669, 274, 303, 324, 87, 3664, -1, -1, 1663, 3965, 2166, 79, 4167, 1670, 4136, 1663, 2553, 12194, -1, 37148, 79, 474, 1670, 24496, -1, -1, 2227, 77, 79, 18935, 1670, 247, -1, 2227, 77, 79, 1841, 1670, 359, -1, 2227, 77, 79, 3795, 32213, 130, 5633, 1670, -1, 2227, 77, 79, 474, 1670, 19153, -1, 2227, 77, 79, 1868, 100563, -1, 2227, 77, 79, 4167, 124, 16102, 130, 8580, 1670, -1, -1, 64, 315, 3923, 1422, 87, 110, 93, 848, -1, 2232, 3087, 1033, 257, 8580, 1085, 1670, 1162, 3453, 1453, 79, 1868, 10, -1, 4720, 64, 163, 2300, 1413, 436, 257, 77, 106, -1, 64, 2300, 6, 9336, 130, 64, 1162, 77, 79, 20467, 10, -1, -1, 130, 1196, 1670, 5353, 2395, 4136, 1663, 2553, 12194, -1, 413, 406, 4167, 2395, 1670, 1162, 3453, 56395, 79, 2396, -1, -1, 2227, 77, 79, 18935, 1670, 247, -1, 2227, 77, 79, 1841, 1670, 359, -1, 2227, 77, 79, 3795, 32213, 130, 5633, 1670, -1, 2227, 77, 79, 474, 1670, 19153, -1, 2227, 77, 79, 1868, 100563, -1, 2227, 77, 79, 4167, 124, 16102, 130, 8580, 1670, -1, -1, 2227, 77, 79, 18935, 1670, 247, -1, 2227, 77, 79, 1841, 1670, 359, -1, 2227, 77, 79, 3795, 32213, 130, 5633, 1670, -1, 2227, 77, 79, 474, 1670, 19153, -1, 2227, 77, 79, 1868, 100563, -1, 2227, 77, 79, 4167, 124, 16102, 130, 8580, 1670, -1, -1, 64, 315, 3923, 1422, 87, 110, 93, 848, -1, 2232, 3087, 1033, 257, 8580, 1085, 1670, 1162, 3453, 1453, 79, 1868, 10, -1, 4720, 64, 163, 2300, 1413, 436, 257, 77, 106, -1, 64, 2300, 6, 9336, 130, 64, 1162, 77, 79, 20467, 10, -1, -1, 1663, 3965, 2166, 79, 4167, 1670, 4136, 1663, 2553, 12194, -1, 37148, 79, 474, 1670, 24496, -1, -1, 2227, 77, 79, 18935, 1670, 247, -1, 2227, 77, 79, 1841, 1670, 359, -1, 2227, 77, 79, 3795, 32213, 130, 5633, 1670, -1, 2227, 77, 79, 474, 1670, 19153, -1, 2227, 77, 79, 1868, 100563, -1, 2227, 77, 79, 4167, 124, 16102, 130, 8580, 1670, -1, -1, 2227, 77, 79, 18935, 1670, 247, -1, 2227, 77, 79, 1841, 1670, 359, -1, 2227, 77, 79, 3795, 32213, 130, 5633, 1670, -1, 2227, 77, 79, 474, 1670, 19153, -1, 2227, 77, 79, 1868, 100563, -1, 2227, 77, 79, 4167, 124, 16102, 130, 8580, 1670, -1, -1, 2227, 77, 79, 18935, 1670, 247, -1, 2227, 77, 79, 1841, 1670, 359, -1, 2227, 77, 79, 3795, 32213, 130, 5633, 1670, -1, 2227, 77, 79, 474, 1670, 19153, -1, 2227, 77, 79, 1868, 100563, -1, 2227, 77, 79, 4167, 124, 16102, 130, 8580, 1670]

    my_dict, secret_message = text_decoder("A_Tale_Of_Two_Cities.txt", secret_indices)
    print(my_dict)
    print(secret_message)

    with open("decoded_message.txt", "w") as f:
        f.write(secret_message)

def quiz_sample_solution(): # I am a bit lazy today so program will not be organized the best...
    # M = S (so U = A or a 20 shift Caesar cipher)
    caesar_cipher_dict = {'a':'g' , 'b':'h' ,'c':'i' ,'d':'j' ,'e':'k' ,'f':'l' ,'g':'m' ,'h':'n' ,'i':'o' ,'j':'p' ,'k':'q' ,'l':'r' ,'m':'s' ,'n':'t' ,'o':'u' ,'p':'v' ,'q':'w' ,'r':'x' ,'s':'y' ,'t':'z' ,'u':'a' ,'v':'b' ,'w':'c' ,'x':'d' ,'y':'e' ,'z':'f'}
    # I'm sure you could fill this out algorithmically but again I'm a bit lazy today and this might be a bit too difficult for students...

    file_contents = []
    # Now read in the file...
    with open("secret_code.txt", "r") as f:
        file_contents = []
        for line in f:
            for character in line:
                if character.lower() in caesar_cipher_dict: # If the lowercase character is in the dictionary (i.e. it is a letter)
                    if (character.isupper()):
                        file_contents.append(caesar_cipher_dict[character.lower()].upper()) # Go lower for key (getting the caesar-shifted letter) then convert value to upper
                    else:
                        file_contents.append(caesar_cipher_dict[character.lower()]) # Get the corresponding caesar-shifted letter
                else: # Non-alphabetical
                    file_contents.append(character) # Just append the character without modification
    print(file_contents) # Now we have a list

    secret_message = []

    for i in range(len(file_contents)):
        if (i != 0): # We skip the first letter...
            if (file_contents[i].isupper() and file_contents[i-1] != "\n"): # Then out of place...
                secret_message.append(file_contents[i])

    secret_message_string = ''.join(secret_message) # Quick hack to get into string. Could just use loops instead...

    with open("code_cracked.txt", "w") as f:
        f.write("https://tinyurl.com/" + secret_message_string)
                

if __name__ == '__main__':
    quiz_sample_solution()

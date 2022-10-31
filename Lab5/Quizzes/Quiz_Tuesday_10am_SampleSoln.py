def TeletubbyDecomposer(teleteletubbytubby):
    teletubbies = ["Tinky Winky", "Dipsy", "Laa-Laa", "Po"]
    #print(teleteletubbytubby) # Uncomment this if you want to track the recursive calls

    if (teleteletubbytubby in teletubbies): # Base Case (a single teletubby)
        return [teleteletubbytubby]
    else: # Recursive Call
        if (teleteletubbytubby[0] == "P"): # Po Recursive Call Case
            return ["Po"] + TeletubbyDecomposer(teleteletubbytubby[len("Po"):])
        elif (teleteletubbytubby[0] == "T"): # Tinky Winky Recursive Call Case
            return ["Tinky Winky"] + TeletubbyDecomposer(teleteletubbytubby[len("Tinky Winky"):])
        elif (teleteletubbytubby[0] == "L"): # Laa-Laa Recursive Call Case
            return ["Laa-Laa"] + TeletubbyDecomposer(teleteletubbytubby[len("Laa-Laa"):])
        else: # Dipsy Recursive Call Case
            return ["Dipsy"] + TeletubbyDecomposer(teleteletubbytubby[len("Dipsy"):])

if __name__ == "__main__":
    teleteletubbytubby = "PoPo"
    print(TeletubbyDecomposer(teleteletubbytubby))
    teleteletubbytubby = "Tinky Winky"
    print(TeletubbyDecomposer(teleteletubbytubby))
    teleteletubbytubby = "Laa-LaaLaa-LaaLaa-Laa"
    print(TeletubbyDecomposer(teleteletubbytubby))
    teleteletubbytubby = "DipsyDipsyDipsyDipsy"
    print(TeletubbyDecomposer(teleteletubbytubby))

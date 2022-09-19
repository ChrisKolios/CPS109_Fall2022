def harmony_func(a, b, c):
    if (a == b):
        return "There is harmony"
    elif (a > (2*(b**2))) or (b > (2*(a**2))):
        return "There is discord"
    else: # Technically not needed as return will exit if either of the above are True
        return c

print(harmony_func(2, 2, "Hello World"))
print(harmony_func(2, 9, "Hello World"))
print(harmony_func(2, 7, "Please print me"))


def m_harmony_func(a, b, c, d):
    if (a == b):
        return "There is harmony"
    elif (a > (2*(b**2))) or (b > (2*(a**2))):
        return "There is discord"
    else: # Technically not needed as return will exit if either of the above are True
        if (len(c) == len(d)):
            return "There is string harmony"
        elif (len(c) > len(d)):
            return c
        else:
            return d

print(m_harmony_func(2, 2, "Hello World", "Hello World"))
print(m_harmony_func(2, 9, "Hello World", "Greetings World"))
print(m_harmony_func(2, 7, "Balance", "Harmony"))
print(m_harmony_func(2, 7, "I am longer", "I am short"))
print(m_harmony_func(2, 2, "Drums", "Drums in the deep"))

import math
# Let's find an arbitrary root for any number!

if __name__ == "__main__":
    # Type safety? Never heard of her.
    # Let's say I left this in as an example of nested type conversion
    num = float(abs(int(input("What number do you want the root for?\n"))))
    root = float(abs(int(input("And what root do you want to find for it?\n"))))

    lo = 0
    hi = max(num, 1.0)

    guess = (lo + hi) / 2
    e = 0.0001
    error = guess ** root - num

    # So for those who are confused by this (I ripped it out of the p. 33 in the textbook)
    # Think of this while loop like a pendulum, with the root specified above
    # as the centre. The program will swing back and forth past the real root,
    # adjusting its swing, until eventually it lands approximately in the centre.
    # (On the root).
    while abs(error) > e :
        if error < 0 :
            lo = guess
        else :
            hi = guess

        guess = (lo + hi) / 2
        error = guess ** root - num

    print('The approximate', root, 'root of ', num, 'is', guess)
    
    # This example can be a bit tricky to understand. Let's trace through an example input to see exactly what's going on here.
    
    # Consider num = 9, and root = 2 (i.e. we want to find the square root of 9, which is, of course, 3)
    # Then lo = 0, hi = 9, guess = 4.5, e = 0.0001, and error = (4.5)^2 - 9 = 11.25
    
    # abs(11.25) > 0.0001, so we then check and notice 11.25 > 0, and so now hi = 4.5
    # Now guess = (0 + 4.5) / 2 = 2.25, and error = 2.25^2 - 9 = -3.9375
    
    #  abs(-3.9375) > 0.0001, so we check and notice -3.9375 < 0, so now lo = 2.25
    # Now guess = (2.25 + 4.5) / 2 = 3.375, and error = 3.375^2 - 9 = 2.390625

    # abs(2.390625) > e, so we check and notice 2.390625 > 0, so now hi = 3.375
    # Now guess = (2.25 + 3.375) / 2 = 2.8125, and error = 2.8125^2 - 9 = -1.08984375
    
    # Cont...

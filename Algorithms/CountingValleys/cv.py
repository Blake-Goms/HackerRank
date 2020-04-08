def countingValleys(n, s):
    # s is a string of Us and Ds 
    # keep track of the height 
    height = 0
    # keep track of number of valleys 
    valleys = 0
    # loop through the string s 
    for step in s:
        # depending on whether we see a U or a D 
        # only need to keep track of one
        if step == 'U':
            # update the height counter accordingly 
            height += 1
            # if the height counter returns to 0
            if height == 0:
                valleys += 1
        else:
            height -= 1
            
    return valleys


x = countingValleys(8, "UDDDUDUU") 
print(x) # expect 1

z = countingValleys(12, "DDUUDDUDUUUD") 
print(z) # expect 2
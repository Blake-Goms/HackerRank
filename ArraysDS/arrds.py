def reverseArray(a):
    # slice the array in reverse order
    # slicing by itself does not mutate original list, set to newList
    # newList = a[::-1] # this is saying give me the whole list, but "step" in reverse order(values are all but not listed in x:x:-1)
    # return newList

    # reverse array alternative using built-in List method
    # this also happens to be much more performant
    # newList = reversed(a)
    # return newList
    
    # reversed using list
    # this lets reversed exhaust the iterator, then list takes the result and stores 
    # it as a list, then return that list
    newList = list(reversed(a))
    # return newList
    print(newList)


test = [0,1,2,3,4,5,6]
reverseArray(test)
test2 = [-4, 3, -9, 0, 4, 1]
reverseArray(test2)
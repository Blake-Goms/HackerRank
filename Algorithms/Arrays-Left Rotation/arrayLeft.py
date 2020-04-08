def rotLeft(a, d):
    tempArray = []
    temp = 0
    for i in range(len(a)): 
        temp = a.pop(0)
        tempArray.append(temp)
    copyArray = a
    finalArray = copyArray.extends(tempArray)
    print(finalArray)
    return finalArray


test = [1,2,3,4,5]
rotLeft(test,4)
# test2 = [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]
# rotLeft(test2, 10)
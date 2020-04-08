def aVeryBigSum(ar):
    sum = 0
    for i in range(len(ar)):
        sum += ar[i]
    print('sum of ints in array:' , sum)
    return sum


test = [1,2,3,4,5]
aVeryBigSum(test)
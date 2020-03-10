# https://www.hackerrank.com/challenges/plus-minus/problem

'''
You must print the following  lines:
A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.

Test are from 0 < n <=100
'''

def plusMinus(arr):
    # using the length
    length = len(arr) or 0
    # use these to keep track
    pos = 0
    negs = 0
    zeros = 0
    # only run in these conditions
    if(length > 0 or length <= 100):
        for i in arr:
            if(i > 0):
                pos += 1
            elif(i < 0):
                negs += 1
            else:
                zeros += 1
    else:
        print('Passed in argument falls out of testing range')
        
    print('Average number of positives is: ', pos / length)
    print('Average number of negatives is: ', negs / length)
    print('Average number of zeros is: ', zeros / length)
    
test = [-4, 3, -9, 0, 4, 1]
plusMinus(test)
test2 = [1, 2, 3, -1, 6 ,-2, -3, 0, 0]
plusMinus(test2)
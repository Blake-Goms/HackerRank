# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def birthdayCakeCandles(ar):
    height = max(ar)
    count = 0
    for i in range(len(ar)):
        if ar[i] == height:
            count += 1
    print(count)
    return count


birthdayCakeCandles([4,3,2,1,4])
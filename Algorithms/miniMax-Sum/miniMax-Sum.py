def miniMaxSum(arr):
    sum = 0
    for i in range(len(arr)):
        # add value of index to sum
        sum += arr[i]
    # once we find the sum all we need to do is subtract 
    # the highest and lowest values to find the max/min
    print(sum - max(arr), sum - min(arr))
    
    
miniMaxSum([1,2,3,4,5])
// https://www.hackerrank.com/challenges/mini-max-sum/problem
function miniMaxSum(arr) {
    let sum = 0
    for(let i = 0; i < arr.length; i++){
        sum += arr[i]
    }
    const max = sum - Math.max.apply(Math, arr)
    const min = sum - Math.min.apply(Math, arr)
    // below does not work because it is not expecting an array = NaN
    // const max = sum - Math.max(arr)
    // const min = sum - Math.min(arr)
    // alternative is destructure array to avoid NaN
    // const max = sum - Math.max(...arr)
    // const min = sum - Math.min(...arr)
    console.log(max, min)
}

miniMaxSum([1,2,3,4,5])
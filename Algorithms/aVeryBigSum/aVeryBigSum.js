// https://www.hackerrank.com/challenges/a-very-big-sum/problem

function aVeryBigSum(ar) {
    let sum = 0
    for(let i = 0; i < ar.length; i++){
        sum += ar[i]
    }
    console.log(sum)
    return sum
}

const test = [1,2,3,4,5]
aVeryBigSum(test)
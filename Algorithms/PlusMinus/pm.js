// https://www.hackerrank.com/challenges/plus-minus/problem

/*
You must print the following  lines:
A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.

Test are from 0 < n <=100
*/

function plusMinus(arr) {
    const length = arr.length || 0
    let pos = 0, negs = 0, zeros = 0
    if (length > 0 && length <= 100) {
        arr.map(i => {
            if(i > 0){
                pos++
            }
            else if (i < 0){
                negs++
            }
            else {
                zeros++
            }
        })
    }
    console.log(pos / length);
    console.log(negs / length);
    console.log(zeros / length);
}

const test = [-4, 3, -9, 0, 4, 1]
plusMinus(test)
const test2 = [1, 2, 3, -1, 6 ,-2, -3, 0, 0]
plusMinus(test2)
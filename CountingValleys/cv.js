// https://www.hackerrank.com/challenges/counting-valleys/problem?h_r=internal-search

// Complete the countingValleys function below.
function countingValleys(n, s) {
//  keep track of height
let height = 0;
//  keep track of valleys
let valleys = 0;
// split the characters so you can compare them
let arr = s.split('')

for(let step = 0; step < arr.length; step++){
    if(arr[step] === 'U'){
        height += 1;
        if (height === 0) {
            valleys += 1;
        }
    } else {
        height -= 1;
    }   
}
    
return valleys
}

let x = countingValleys(8, "UDDDUDUU") 
console.log(x) // expect 1

let z = countingValleys(12, "DDUUDDUDUUUD") 
console.log(z) // expect 2
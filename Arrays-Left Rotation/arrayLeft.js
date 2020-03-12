// https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_r=internal-search
function rotLeft(a, d) {
    // a is the array
    // d is number of rotations
    // IDEA
    // Using a temp array, loop through the parameter to add 
    // the values temporarily. Have a temp to store the returned element
    let tempArray = []
    let temp = 0
    for(let i = 0; i < d; i++){
        temp = a.shift()
        tempArray.push(temp)
    }
    // create another array to loop through and copy the altered original array
    const copyArray = a
    for(let i = 0; i < a.length; i++){
        temp = a.shift()
        copyArray.push(temp)
    }
    //  creating a final array, concat(join) together the previous arrays
    const finalArray = copyArray.concat(tempArray)
    console.log(finalArray)
    return finalArray
}




const test = [1,2,3,4,5]
rotLeft(test,4)
const test2 = [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]
rotLeft(test2, 10)
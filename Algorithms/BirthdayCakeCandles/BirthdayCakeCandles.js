function birthdayCakeCandles(ar) {
    // use built in method to find max value, spread in array to avoid errors
    const height = Math.max(...ar)
    let count = 0
    for(let i = 0; i < ar.length; i++){
        if(ar[i] === height){
            count += 1
        }
    }
    console.log(count)
    return count
}
const array = [4,3,2,1,4]
birthdayCakeCandles(array) 
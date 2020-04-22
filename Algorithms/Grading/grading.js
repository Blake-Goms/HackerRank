function gradingStudents(grades) {
    // Write your code here
    let roundedGrades = []
    let temp = 0
    for(let g = 0; g < grades.length; g++){
        if ((grades[g] >= 38) && (grades[g] % 5 >= 3)){
            temp = grades[g] + 5 - (grades[g] % 5)
            roundedGrades.push(temp)
        }
        else {
            roundedGrades.push(grades[g])
        } 
    }
    console.log(roundedGrades)
    return roundedGrades
}



gradingStudents([73,67,38,33])
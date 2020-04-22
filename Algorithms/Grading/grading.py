#  https://www.hackerrank.com/challenges/grading/problem
def gradingStudents(grades):
    # Write your code here
    roundedGrades = []
    for g in grades:
        if g >= 38 and g % 5 >= 3:
            g = g + 5 - (g % 5)
            roundedGrades.append(g)
        else:
            roundedGrades.append(g)
    print(roundedGrades)
    return roundedGrades


gradingStudents([73,67,38,33])
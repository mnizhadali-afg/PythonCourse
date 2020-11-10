import math

# Complete the 'gradingStudents' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.

def gradingStudents(grade):
    # Write your code here
    rounded = math.ceil(grade / 5) * 5
    if ((rounded - grade) < 3):
        return rounded
    elif ((rounded - grade) == 3) or ((rounded - grade) > 3):
        return grade
    elif (grade <= 35):
        return grade

n = int(input("Enter the grade: "))
res = gradingStudents(n)
if (res > 100):
    print("Invalid Grade.")
elif (res < 38):
    print("Failed: ", res)
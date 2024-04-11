#1. Python List Yransformation
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
def Average(grades):
    return sum(grades)/ len(grades)
print("Average of the grades =")
print(Average(grades))
for i in range(len(grades)):
    if grades[i] <= 80:
        grades[i] = "failed"
print(grades)
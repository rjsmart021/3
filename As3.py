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
#Task 1: Given the list of temperatures:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103,104,105, 106]
print('week 2', temperatures[7:14])
#Task2
for i in range(len(temperatures)):
    if temperatures[i] >= 100:
     print(temperatures[i])
#Task3
temperatures.sort(reverse=True)
print(temperatures[4:11])
#3.Deep Dive into Python Lists
#Task 1
students = ["John", "Doe", "Jane", "Smith"]
grades = [85 ,90 ,78 ,88]
activities = ["Football", "Music", "Art", "Dance"]

print(students[0], grades[0], activities[0])
#Task 2
print("students_approved")
print(students[1:4])
students_approved = students[1:4]
print(students_approved)


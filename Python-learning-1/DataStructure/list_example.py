student_names = []
student_names =["Mark", "katarina", "jessica"]
print(student_names)
print(student_names[0]=="Mark")
print(student_names[1]=="katarina")
print(student_names[2]=="jessica")
# Modify Existing StudentList
student_names[0]="James"
print(student_names)
# Adding New Student in List
student_names.append("Homer")
print(student_names)

# Check is katarina still there
print("katarina" in student_names)

# Print the total number of student in list
print(len(student_names)) 

# Delete student from list
del student_names[2]
print(student_names)

# List Slicing
print(student_names[1:])
print(student_names[1:-1])
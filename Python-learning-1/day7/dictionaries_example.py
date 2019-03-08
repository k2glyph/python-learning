student = {
    "name": "John",
    "student_id": 15163,
    "feedback":None
}
print(student)
print(student["name"])
print(student["feedback"])
all_students = [
	{ "name": "john", "student_id": 15163 },
	{ "name": "katarina", "student_id": 63112 },
	{ "name": "Jessica", "student_id": 30021 }
]
print(all_students)

for student in all_students:
	print(student.get("name"))
	print(student.keys())
	print(student.values())

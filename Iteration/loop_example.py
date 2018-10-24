student_names =["Mark", "katarina", "jessica"]
# For each loop example for 
for name in student_names:
    print("Student name is {0}".format(name))
print("\n")
# traditional for loop with range function 
for index in range(len(student_names)):
    print("Student name is {0}".format(student_names[index]))
print("\n")
for index in range(0, len(student_names), 2):
    print("Student name is {0}".format(student_names[index]))

for name in student_names:
    if name == "Mark":
        print("Found him!"+name)
    print("Currently testing"+ name)

# While loop
print("\n")
x=0
while x<len(student_names):
    print(f"Student name is: {student_names[x]}")
    x+=1

print("\n")
x=0
while True:
    if(x==3):
     break
    print(f"Student name is: {student_names[x]}")
    x+=1
    
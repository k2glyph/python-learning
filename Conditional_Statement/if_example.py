number = 5
if number ==5:
    print("Number is 5")
else:
    print("Number is Not 5")
text = "Python"
# Example of Truthy value
if text:
    print("Text is defined and Truthy")

# Example None 
aliens_found=None
if aliens_found:
    print("Aliens found")
else:
    print("Aliens still not found")

# Not operator
is_java_god=True
if not is_java_god:
    print("Java is God")
else:
    print("No Java is not God")

# And | or Operator
number = 3
python_course = True

if number ==3 and python_course: # Both value must be true
    print("Both are true")

if number ==17 or python_course: # Among both of this value one must be true
    print("one is only true")

# Ternary if Statements

a=1
b=2
print("bigger" if a>b else "smaller")


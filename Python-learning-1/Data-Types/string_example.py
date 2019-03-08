
name = "Dinesh Katwal"
machine = "Welcome machine"
print('Hello World' == "Hello World" == """Hello World""")
print("hello".capitalize()== "Hello")
print("hello".upper()== "HELLO")
print("hello".replace('e', 'a')=="hallo")
print("hello".isalpha()==True)
print("123".isdigit()==True) # Useful when converting to int
print("some, csv, values".split(",") == ["some", "csv", "values"])

# String formating
greeting = "Nice to meet you {0}. I am {1}"
print(greeting.format(name, machine))
print(f"Nice to meet you {name}. I am {machine}")

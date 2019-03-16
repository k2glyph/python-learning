# Demonstrate hashtable usage.
# Create a hashtable
items1= dict({"key1":1, "key2": 2, "key3": "three"})
print(items1)
# Creating progressive hash table
item2= {}
item2["key1"]=1
item2["key2"]=2
item2["key3"]=3
print(item2)

# Finding items that doesn't exist in the hash table

# print(item2["key6"])

# Replace key value
item2["key2"]="two"
print(item2)

# Iterating in the dictinary
for key, value in item2.items():
    print("key:", key, "value:", value)

    
users = {"id": 1, "age": 30, "city" : "New York"}

print(users)

# accessing values from dictionary using key
# print(users["names"])
print(users.get("age","unknown"))  # using get method to access values from dictionary

# checking if key is present in dictionary or not
age = users.get("age")
if age:
    print("Age is present in dictionary")
    print(f"Age: {age}")
else:
    print("not available")

# checking
print("age" in users)  # using in operator to check if key is present in dictionary or not

# view objects in dictionary
print(users.keys())  # returns view object of keys in dictionary
print(users.values())  # returns view object of values in dictionary
print(users.items())  # returns view object of key-value pairs in dictionary
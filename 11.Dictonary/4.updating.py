users = {"id": 1, "age": 30, "city" : "New York"}

# add, update,remove
users["name"] = "Joy"  # adding new key-value pair to dictionary
users.update({"age": 21, "city": "Los Angeles", "work": "Engineer"})  # updating existing key-value pairs or adding new ones in dictionary 
print(users)

city = users.pop("salary", "not found")  # removing key-value pair from dictionary using pop method
print("City:", city)  # removing key-value pair from dictionary using pop method
print(users)

users.popitem()  # removing last inserted key-value pair from dictionary using popitem method
print(users)
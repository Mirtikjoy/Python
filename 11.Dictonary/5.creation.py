my_dict = {
    "id" : None,
    "age" : None,
    "city" : None,
    "salary" : None
}

my_dict.fromkeys(["id", "age", "city", "salary"], None)  # creating dictionary using fromkeys method
my_dict["id"] = 1

print(my_dict)
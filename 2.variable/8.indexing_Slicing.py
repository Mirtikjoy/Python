name = "mirtik Joy"
print(name[0::2])

num = "123-768-073-296"

print(num[0:15:2])

name1 = "niket", "joy", "mirtik", "pariya", "harsh", "wilson", "pranav"
# cvv = name1.split(",")
# print(cvv)


names = name1[2]
print(names, name1[4], name1[6])


# date of birth
dob = "2005-09-01"

print(f"year of birth: {dob[:4]}")  # extracting year using slicing

print(f"Month of birth: {dob[5:7]}")  # extracting month using slicing

print(f"date of birth: {dob[8:10]}")  # extracting date using slicing

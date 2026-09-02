person = ['Mirtik joy Molsom', 21, 'B.tech', 'IT', '24BTIT019', 'Rai University']

# name = person[0]
# age = person[1]
# branch = person[2]
# specialisation = person[3]
# uID = person[4]
# university = person[5]

name, age, branch, specialization, UID_number, university = person
print(len(name))

# using asterisk i.e, * for unpacking


name, *details, UID_number, university = person
print(name)
print(details)
print(UID_number)
print(university)

name,_,branch,*details,university = person
print(name)
print(branch)
print(details)
print(university)
name = input("please enter your name: ")
age = input("please enter your age: ")
email = input("please enter your email: ")


# any is a funtion that returns a bool(Boolean) value i.e, True if any one if it's instances is filled else return value False
vallidation = any([name,age,email])
print(vallidation)

print(f"your name is {name}")
print(f"your age is {age}")
print(f"your email is {email}")

# All is a funtion that returns a bool(Boolean) value i.e, True when everything is validate else return False
university = input("please enter your university name: ")
university_Address = input("please enter your address: ")
university_email = input("please enter your university emailId: ")

university_Vallidation = all([university,university_Address,university_Address])

print(f"\nuniversity_Vallidation")

print(f"university: {university}")
print(f"address: {university_Address}")
print(f"university email Id: {university_email}")
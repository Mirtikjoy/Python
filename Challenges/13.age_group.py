age = int(input("please enter your age: "))

def age_group(age):
    if age <=13:
        return "Child"
    elif age <= 20:
        return "Teen"
    elif age <= 60:
        return "Adult"
    else:
        return "Senior"


age_groups = age_group(age)
print(f"He/she is {age_groups}")
first_name = input("please enter your first name: ")
middle_name = input("please enter your middle name: ")
last_name = input("please enter your last name: ")

def names(first,middle="",last="N/a"):
    first_N = first.strip().lower().capitalize()
    middle_N = middle.strip().lower().capitalize()
    last_N = last.strip().lower().capitalize()
    full_Name = first_N +" "+ middle_N +" "+ last_N
    return full_Name


your_name = names(first_name,middle_name,last_name)
print("your name: ",your_name)
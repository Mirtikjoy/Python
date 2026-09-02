name = input("Enter your name: ")
age = int(input("enter your age:"))

if name != "":
    print(f"Your name is {name}")
else:
    print("please enter your name.")


if age.isdigit():
    age = int(age)

    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
else:
    print("Invalid input! Please enter your age as a number.")

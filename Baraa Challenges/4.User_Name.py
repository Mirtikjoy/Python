user_name = input("Please enter your name: ")

if not user_name.replace(" ", "").isalpha() or len(user_name) < 5 or user_name == "":
    print("Invalid name. Please enter a valid name with at least 5 alphabetic characters.")
else:
    print(f"\nYour name is {user_name}.")


    
email = input("Enter your mail address: ")

if "@" in email and ".com" in email:
    print("Mail address is valid.")
else:
    print("Mail address is invalid. Please enter a valid mail address.")
    
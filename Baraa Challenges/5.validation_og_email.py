# email must be valid
# must not contain space
# should not be empty string
# should not ahve more than one @
# should end with .com, .org, .outlook, .net

email = input("please enter your email address: ")

if " " in email :
    print("email address can not contain spaces!, please enter your valid email address")
elif email == "":
    print("email cannot be empty")
elif not ("@" in email or "." in email):
    print("email must contain @ or .")
elif not email.endswith((".com",".net",".org",".outlook")):
    print("email must end with .com, .net, .org, .outlool")
elif email.count("@") != 1:
    print("@ should not contain more than 1")
elif len(email) > 6:
    print("email id should not exceeds more than 256 length ")
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("email cannot contain special caracters")
else:
    print("your email is valid")
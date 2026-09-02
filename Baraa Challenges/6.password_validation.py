email = input("please enter your email address: ")
password = input("Please enter your password: ")

if " " in email:
    print("email address cannot contain spaces")
elif email == "":
    print("email cannot be empty string! please enter your email address")
elif not email.endswith((".com", ".org", ".net", ".outlook")):
    print("email address must ends with .com, .org, .net, or .outlook")
elif len(email) > 60:
    print("The length of email address cannot exceeds 59 length")
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("email should not contain special characters")
elif email.count("@") != 1:
    print("@ should contain more than 1")
else:
    print("email is valid")

if password == "":
    print("Password cannot be empty string! please enter your password")
elif len(password) < 9:
    print("Password is too short. It must be at least 9 characters long.")
elif password.isdigit() or password.isalpha():
    print("Password cannot be only numbers or only letters. It must contain both atleast one letter or one special character.")
elif not any(char in password for char in "!,@,#,$,%,^,&,*,(,),_,+,=,.,<,>,?,/,|,\\,{,},[,],~,`,;,:,,-"):
    print("Password must contain at least one special character.")
elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")
elif not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter.")
else:
    print("Password is valid.")
    
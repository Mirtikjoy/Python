
i = 0
while i < 3:
    attempt = input("please enter your name:- ")
    answer = input("Do you still would like to continue (yes/no):- ")
    if answer == "yes":
        print(attempt,":")
        print("Glad We're onn the same page")
        break        
    i += 1
else:
    print("sorry, you are out of attempt")

print("Thank you")

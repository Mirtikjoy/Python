name = []
duplicates_Names = []
i = 0
while i < 5:
    new_name = input("please enter your name: ")
    name.append(new_name)

    j = 0
    duplicate = False
    while j < i:
        if name[j] == name[i]:
            duplicate = True
            break
        j += 1

    if duplicate:
        print("you have already enter your name!")
        duplicates_Names.append(name[i])
        name.pop()
        i -= 1
    else:
        print(f"\n The names  are:- {', '.join(name)}")

    i += 1

print(f"The names you have enter are:- {name}")
print(F"Duplicates names found:- {duplicates_Names}")

names = []

while True:
    name = input("please enter your name: ")
    if name == '':
        print('Unknow name')
    else:
        names.append(name)

    choose = input('Do you want to enter more names (yes/No): ')

    if choose == 'yes':
        continue
    else:
        break

print(f"Names:- {', '.join(names)}")
    
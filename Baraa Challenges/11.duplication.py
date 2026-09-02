fruit = []
duplicates = []

i = 0

while i < 5:
    fruit_name = input("Please enter the fruit name: ")

    fruit.append(fruit_name)

    j = 0
    duplicate = False

    while j < i:
        if fruit[j] == fruit[i]:
            duplicate = True
            break

        j += 1

    if duplicate:
        print("Duplicate found!")
        duplicates.append(fruit[i])
        fruit.pop()     # remove duplicate from fruit list
        i -= 1
    else:
        print(f"Fruits are: {', '.join(fruit)}")

    i += 1

print("\nFinal fruits:", ", ".join(fruit))
print("Duplicates:", ", ".join(duplicates))
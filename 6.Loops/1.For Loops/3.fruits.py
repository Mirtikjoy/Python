fruits = ["apple", "banana", "orange", "grape", "kiwi", "mango", "pear", "peach", "plum", "cherry"]

new_fruits = []

for fruit in fruits:
    fruit = fruit.strip().capitalize()
    new_fruits.append(fruit)

print("Fruits: ", ", ".join(new_fruits))
with open('13.input output/practice.txt', 'r') as f:
    data = f.read()

new_data = data.replace("java","Python")
print(new_data)

with open('13.input output/practice.txt', 'w') as f:
    f.write(new_data)
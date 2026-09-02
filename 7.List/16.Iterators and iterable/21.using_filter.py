letters = ['a', 'b',"", 'c', 'd', 9]

print(list(filter(bool, letters)))

str_values = ['sql', 'python', '90', " ", "908"]

# print(list(filter(str.isalpha,str_values)))

for v in filter(str.isalpha,str_values):
    print(v)
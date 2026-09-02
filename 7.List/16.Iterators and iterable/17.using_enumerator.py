# enumerator is a built-in function in python that gives us indices and it's value

letters = ['a','b','c','d']

# print(list(enumerate(letters)))

for index, value in enumerate(letters,start = 1):
    print(index, value,)
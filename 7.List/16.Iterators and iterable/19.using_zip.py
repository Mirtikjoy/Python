letters = ['a','b','c','d']
numbers = [1,2,3,4]

print(list(zip(letters,numbers)))

for l, n in  zip(letters,numbers):
    print(l,n)

numbers = [1,2,3]
letters = ['a','b','c']
names = ["mirtik", "joy", "molsom"]

# using + operators

comb = numbers + letters
print(comb)

# using ,

comb1 = [letters,numbers]
print(comb1)

# using extend method
letters.extend(numbers)
print(numbers)
print(letters)

# using zip()
# Usecase for paring list

comb2 = list(zip(numbers,letters,names))
print(comb2)
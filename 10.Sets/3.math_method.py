a = {20,30,40,50,70}
b = {30,40,50,60}

# Using union() method that returns a new set with all items from both sets
c = a.union(b)
print(a | b)  # shorthand of union method
print(c)  # Output: {20, 30, 40, 50, 60}

a.intersection(b)  # Using intersection() method that returns a new set with items that are common to both sets
print(a.intersection(b))  # Output: {40, 50, 30}

a.difference(b)  # Using difference() method that returns a new set with items that are in the first set but not in the second set
print(a.difference(b)) 
print(a - b)  # shorthand of difference method

a.symmetric_difference(b)  # Using symmetric_difference() method that returns a new set with items that are in either set, but not in both
print(a.symmetric_difference(b))  # Output: {20, 60, 70}
print(a ^ b)  # shorthand of symmetric_difference method
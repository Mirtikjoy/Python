import copy
original = [
    [2, 7],
    [9, 5]
]

#using assignment operators
copy1 = original
print("same objects?", copy1 is original)

# using shallow copy 
copy2 = original.copy()
print("same objects?", copy2 is original)
print("shared list?", copy2[0] is original[0])

# using deep copy 
copy3 = copy.deepcopy(original)
print("same objects?", copy3 is original)
print("shared list?", copy3[0] is original[0])




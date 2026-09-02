import copy

lst = [
    ['a','b'],
    ['f','c']
]

copy_lst = copy.deepcopy(lst)
lst.pop()
copy_lst[1].append(9)

print("original copy:",lst)
print("copy_lst",copy_lst)

def occurance(num):
    item_occ = {}

    for nums in num:
        item_occ[nums] = item_occ.get(nums, 0) + 1

    return item_occ


num = input("Please enter the numbers: ").split()
num = [int(n) for n in num]

print(occurance(num))
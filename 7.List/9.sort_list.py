numbers = [2,3,4,5,9.4,1,7,8,6,10]
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)

new_numbers = sorted(numbers)
reversed_number = sorted(numbers, reverse=True)
print("copy numbers:",new_numbers)
print("Revrese copy numbers:",reversed_number)
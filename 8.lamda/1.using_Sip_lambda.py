# multiply = lambda x : x * 2

# print(multiply(2))

# addition = lambda x, y : x + y
# print(addition( 2,7))

add = lambda *numbers : sum(numbers)

numbers = input("please enter the number: ").split()
numbers = [
    int(number) 
    for number in numbers
    ]

print (add(*numbers))
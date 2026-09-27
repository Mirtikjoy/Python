import statistics
# num = int(input("please enter how many input you want to enter: "))

# newInt = []
# i = 1
# while(i <= num):
#     myint = int(input(f"please enter the {i} number: "))
#     newInt.append(myint)
#     i +=1


numbers = list(map(int, input("Enter numbers: ").split()))
average = statistics.mean(numbers)

print(average)
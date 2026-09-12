import math
numb = int(input("please enter the number: "))

def prime_num(num):
    if num < 2:
        return False

    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

for i in range (2, numb+1):
    if prime_num(i):
        print(i, end=' ')

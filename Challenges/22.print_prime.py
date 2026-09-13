import math
numb = int(input("please enter the number: "))

def prime_num(num):
    if num < 2:
        return False
# math.sqrt give us the square root of the numbers
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

for i in range (2, numb+1):

    """ this is a method to print all the prime number"""
    if prime_num(i):
        print(i, end=' ')

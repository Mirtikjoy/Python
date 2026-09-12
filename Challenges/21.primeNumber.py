numb = int(input("please enter the number: "))

def prime(num):
    if num < 2:
        return False
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


if prime(numb):
    print("The number is prime number")
else:
    print("The number is not prime number")
num = int(input("Please enter the number you wanna check: "))

def isFibonacci(num):
    if num < 0:
        return False  # Fibonacci numbers are non-negative
    
    first, second = 0, 1
    while first <= num:
        if first == num:
            return True
        first, second = second, first + second
    return False

print(isFibonacci(num))

num = int(input("Please enter the number: "))

def fibonacii_series(num):
    """ printing fibonacii series upto the certain user number input
    """

    if num < 0:
        return 0
    if num == 0:
        return 1

    first, second = 0, 1 
    third = []
    
    while first <= num:
        # third = first + second
        # print(third, " ")
        # first = second
        # second = third

        third.append(first)
        first,second = second, first + second
    return third
fibo = fibonacii_series(num)
print(fibo)
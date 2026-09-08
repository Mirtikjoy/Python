numb = int(input("Please enter the number: "))

def sum_odd(num):
    """this should add all the odds numbers
    """

    mynumbs = 0
    odd = 1
    while( odd <= num):
        mynumbs += odd
        odd += 2
    return mynumbs

odds_nums = sum_odd(numb)
print(odds_nums)
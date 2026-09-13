num = int(input("please enter the number: "))

def reverseNum(num):
    """ gives the reverse of the number,
    first we do take the reminder and put it in revnum and delete the last number and it goes as long as number is greater
    than zero
    
    """

    revNumb = 0
    while num > 0:
        digit = num % 10
        revNumb = revNumb * 10 + digit
        num //= 10

    return revNumb

rev_Numbers = reverseNum(num)
print(f"The reverse number is: {rev_Numbers}")
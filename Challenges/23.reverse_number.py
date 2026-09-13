num = int(input("please enter the number: "))

def reverseNum(num):

    revNumb = 0
    while num > 0:
        digit = num % 10
        revNumb = revNumb * 10 + digit
        num //= 10

    return revNumb

rev_Numbers = reverseNum(num)
print(f"The reverse number is: {rev_Numbers}")
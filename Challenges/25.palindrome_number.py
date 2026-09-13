numb = int(input("please enter the number: "))
def palindrome(num):
    original_Number = num
    reverse = 0
    while(num > 0):
        """ checks the palindrome number"""
        lastNumber = num % 10
        reverse = reverse * 10 + lastNumber
        num //= 10
    return reverse == original_Number

isPalindrome = palindrome(numb)

if(isPalindrome):
    print(f"{numb} is a palindrome number")
else:
    print(f"{numb} is not palindrome number")


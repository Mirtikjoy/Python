def no_Of_Digits(num):
    """ this gives us the number of digits in our number for ex = 123 is 3 digits"""

    mydigits = 0
    while(num > 0):
        mydigits += 1
        num //= 10
    return mydigits

def power(num1,num2):
    """ this calculates our power ex power(2,5) so it will go and give us 2^5
    i = 0: result = 1 × 2 = 2

    i = 1: result = 2 × 2 = 4

    i = 2: result = 4 × 2 = 8

    i = 3: result = 8 × 2 = 16

    i = 4: result = 16 × 2 = 32
    """
    result = 1
    i = 0
    while(i < num2):
        result *= num1
        i += 1
    return result


def armstrong_Number(num):
    original_num = num
    no_of_digits = no_Of_Digits(num)
    final_Number = 0
    while(num > 0):
        last_digit = num % 10
        num //= 10
        final_Number += power(last_digit,no_of_digits)
    return final_Number == original_num

numb = int(input("please enter the number: "))

is_Armstrong_Number = armstrong_Number(numb)
if(is_Armstrong_Number):
    print(f"{numb} is armstrong number")
else:
    print(f"{numb} is not armstrong number")
    
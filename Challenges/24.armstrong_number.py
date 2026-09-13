def no_Of_Digits(num):

    mydigits = 0
    while(num > 0):
        mydigits += 1
        num //= 10
    return mydigits

def power(num1,num2):
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
    
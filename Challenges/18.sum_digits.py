num = int(input("please enter the number: "))

def digits(num):
    if num <0:
        return False

    
    sum = 0
    while num != 0:
      """this will add all the digits of the numbers
      """
      sum += num % 10
      num /= 10

    return int(sum)

print(digits(num))
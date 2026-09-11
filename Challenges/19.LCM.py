num1 = int(input("Please enter your number: "))
num2 = int(input("please enter your number: "))

def lcm_cal(num1,num2):

    i = 1
    while (True):
        factors = num1 * i
        if (factors % num2 == 0):
            return factors
        i += 1
print(f"Lcm of two numbers is: {lcm_cal(num1,num2)}")




      
      




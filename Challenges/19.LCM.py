num1 = int(input("Please enter your number: "))
num2 = int(input("please enter your number: "))

def lcm_cal(num1,num2):

    i = 1
    while (True):
        """first the num1 will multiply as long as the loop run 
        and when the reminder match 0 the smallest one, which is divided by numb2 
        """
        factors = num1 * i
        if (factors % num2 == 0):
            return factors
        i += 1
print(f"Lcm of two numbers is: {lcm_cal(num1,num2)}")




      
      




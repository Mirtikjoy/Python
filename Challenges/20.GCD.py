import math
numb1 = int(input('please enter the number: '))
numb2 = int(input("please enter the number: "))

# print(math.lcm(numb1,numb2))
# print(math.gcd(numb1,numb2))

def leasts(num1,num2):
    if (numb1 < numb2):
        return numb1
    else:
        return numb2

def gcd_cal(numb1,numb2):
    """ calculation of greatest common factors
    """

    gcd = 1
    i = 2
    least = leasts(numb1,numb2)
    while (i <= least):
        if (numb1 % i == 0 and numb2 % i == 0):
            gcd = i

        i += 1

    return gcd

mygdc = gcd_cal(numb1,numb2)
print(mygdc)
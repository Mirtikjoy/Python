numb = int(input("please enter the number: "))

def multiply(numb):

    """This code is for multiplication table base on the user input
    """
    for i in range(1,11):
        print(f"{i} X {numb} = {i*numb}")

multiply(numb)


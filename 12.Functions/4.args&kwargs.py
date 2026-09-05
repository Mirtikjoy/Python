# *args and **kwargs allows function to accept a unknown number of arguments


# * = args
def total(*num):
    print(sum(num)) # returns tuples

total(25,10,20)

# ** = kwargs

def user_define(**users):
    print(users)

user_define(user_name = "mirtik joy molsom",
            age = 21,
            country = "india")


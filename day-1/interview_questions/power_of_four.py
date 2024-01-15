import math as mt


def fun(num):
    for x in range (num):
        y = mt.pow(4, x)
        if y==num:
            return True
    return False

num = int(input("Enter number to check if it is a power of four: "))
print(fun(num))
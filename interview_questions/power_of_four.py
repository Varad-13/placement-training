import math as mt

def fun(num):
    for x in range (num+1):
        y = mt.pow(4, x)
        if y>=num:
            if y==num:
                return str(x)
            else:
                return False
    return False

num = int(input("Enter number to check if it is a power of four: "))
print(fun(num))
import math

def  find_roots(a, b, c):
    x = (b*b)-(4*a*c)
    if x >= 0:
        root1 = (-b + math.sqrt((b*b)-(4*a*c)))/2*a
        root2 = (-b - math.sqrt((b*b)-(4*a*c)))/2*a
    else:
        return("No real roots!")
    return(root1, root2)


if __name__ == "__main__":
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=int(input("Enter c: "))
    print(find_roots(a,b,c))
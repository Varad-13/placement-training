pi = 3.14

def area(radius):
    return pi*square(radius)
def square(num):
    return num*num

if __name__ == "__main__":
    r = int(input("Input radius of the circle: "))
    print(area(r))
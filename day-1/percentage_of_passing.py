def percentage(x, y):
    return (x*100)/y

if __name__ == "__main__":
    total = int(input("Enter total marks:"))
    passing = int(input("Enter passing marks:"))
    print("Percentage of passing is", percentage(passing, total))
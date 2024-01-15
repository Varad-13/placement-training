start = int(input("Start: "))
end = int(input("End: "))
mul=1
add=0

for x in range(start, end+1, 1):
    if x%2==0:
        mul*=x
    else:
        add+=x

print(mul)
print(add)
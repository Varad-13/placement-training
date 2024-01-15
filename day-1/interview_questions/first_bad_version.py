#Using binary search
n = [1, 2, 3, 4, 5, 6]

def isBadVersion(version):
    if version>=4:
        return True
    else:
        return False


max = len(n)
min = 1
for x in range(min, max+1, 1):
    mid = int((max+min)/2)
    if isBadVersion(n[mid]):
        max = mid
    else:
        min = max
print(n[mid], "is the first bad version")
arr1 = [2, 3, 10, 10]
arr2 = [2, 3, 4, 10]

for x in range(len(arr1)-1, -1, -1):
    for y in range(len(arr2)-1, -1, -1):
        if arr1[x]==arr2[y]:
            arr1.pop(x)
            arr2.pop(y)
            break

print(arr1, arr2)
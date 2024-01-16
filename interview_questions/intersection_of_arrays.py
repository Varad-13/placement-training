arr1 = [2, 3, 10, 10]
arr2 = [2, 3, 4, 10]
output = []
for x in range(len(arr1)):
    for y in range(len(arr2)):
        if arr1[x]==arr2[y]:
            output.append(arr1[x])
            break

print(output)
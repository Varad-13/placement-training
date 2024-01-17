arr = [4, 4, 2, 4, 3]
result = 0

for x in range(len(arr)):
    unique_set = set()
    for y in range(x+1, len(arr)):
        if arr[x] != arr[y] and arr[y] not in unique_set:
            for z in range(y+1, len(arr)):
                if arr[z] != arr[y] and arr[z] != arr[x] and arr[z] not in unique_set:
                    print([arr[x], arr[y], arr[z]])
                    result += 1
                    unique_set.update([arr[x], arr[y], arr[z]])

print(result)

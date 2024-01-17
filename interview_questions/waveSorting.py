def checkWave(arr):
  for i in range(1, len(arr), 2):
    if arr[i-1] > arr[i] and arr[i+1] > arr[i]:
      pass
    else:
      return False
  return True

def createWave(arr):
  arr.sort()
  arr1 = []
  arr2 = []
  result = []
  min = 0
  max = len(arr)-1
  if max%2 != 1:
    mid = int((max/2))
  else:
    mid = upper(max/2)
  for i in range(0, mid):
    arr1.append(arr[i])
  for i in range(mid, max+1):
    arr2.append(arr[i])
  for i in range(len(arr1)):
    result.append(arr2[i])
    result.append(arr1[i])
  if len(arr) != len(result):
    result.append(arr2[-1])
  return result

# keep this function call here 
print(checkWave(createWave(input())))
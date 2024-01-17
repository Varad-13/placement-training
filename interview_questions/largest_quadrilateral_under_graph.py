def HistogramArea(hist):
  result = []
  temp = hist
  for x in range(len(hist)+1):
    if len(temp)>1:
      x = temp.pop()
      if temp[0] > x:
        pass
      else:
        temp.pop(0)
        temp.append(x)
      area1, area2 = max(temp), len(temp)*min(temp)
      result.append(max(area1, area2))
  return max(result)

# keep this function call here 
print(HistogramArea(input()))
def biggest(arr):
  big=arr[0]
  for i in range(1,len(arr)):
    if big <arr[i]:
      big=arr[i]
    else:
      continue
  return big

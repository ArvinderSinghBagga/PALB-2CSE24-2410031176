def minMax(arr):
    if not arr:
        return None
    min_value = arr[0]
    max_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
        elif arr[i] > max_value:
            max_value = arr[i]
            
    return [min_value, max_value]

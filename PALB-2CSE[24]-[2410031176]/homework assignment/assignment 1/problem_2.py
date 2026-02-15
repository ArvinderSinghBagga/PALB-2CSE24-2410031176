def maxminarr(arr):
    max_val=arr[0]
    min_val=arr[0]
    for x in range(len(arr)):
        if arr[x]<min_val:
            min_val=arr[x]
        elif max_val<arr[x]:
            max_val=arr[x]
    return max_val,min_val      
b=[1,2,3,8,6,5,7,0]
maximum_element,minimum_element=maxminarr(b) 
print(maximum_element,minimum_element) 

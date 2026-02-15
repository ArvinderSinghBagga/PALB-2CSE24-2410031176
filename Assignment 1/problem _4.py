def Union(a, b):
    
    merge = a + b
    
    
    merge.sort()
    if not merge:
        return []
    
    result = [c[0]]
    for i in range(1, len(merge)): 
        if merge[i] != merge[i-1]:
            result.append(merge[i])
            
    return result

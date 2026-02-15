def twoSum(nums, target):
    prev_map = {} 
    
    for i, n in enumerate(nums):
        diff = target - n
        
        if diff in prev_map:
            return [prev_map[diff], i]
        
        prev_map[n] = i
nums_list = [2, 7, 11, 15]
target_val = 9

indices = twoSum(nums_list, target_val)
print(f"Indices: {indices}")     

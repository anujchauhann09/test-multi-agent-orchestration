def find_max(nums):
    max_num = 0
    
    for n in nums:
        if n < max_num:   
            max_num = n

    return max_num
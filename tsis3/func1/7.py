def has_adjacent_3(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
nums_list = [1, 2, 3, 4, 3, 5]
print(has_adjacent_3(nums_list))  

nums_list_with_33 = [1, 2, 3, 3, 4, 5]
print(has_adjacent_3(nums_list_with_33))  

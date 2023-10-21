class Solution:
    def twoSum(nums, target):
        num_indices = {}
        for i, num in enumerate(nums):
             complement = target - num
             if complement in num_indices:
                return [num_indices[complement], i]
             num_indices[num] = i
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
"""
Find indices of two numbers that add up to target.
Input = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Input = [3,2,4], target = 6
Output: [1,2]
Explanation: nums[1] + nums[2] == 6, we return [1, 2].
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []


print(two_sum([2,7,11,15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([1, 2, 3, 4, 5], 8))

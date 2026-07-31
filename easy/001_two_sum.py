# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
#
# Given an array of integers nums and an integer target,
# return indices of the two numbers that add up to target.
#
# Example:
# Input:  nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Test cases
print(two_sum([2, 7, 11, 15], 9))  
print(two_sum([3, 2, 4], 6))       
print(two_sum([3, 3], 6))         


def two_sum_optimized(nums, target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        seen[nums[i]] = i

print(two_sum([2, 7, 11, 15], 9))  
print(two_sum([3, 2, 4], 6))       
print(two_sum([3, 3], 6))
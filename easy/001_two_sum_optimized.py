# Problem 1: Two Sum (you already solved this)
# But here's the optimized O(n) version for reference
# Input: nums = [2,7,11,15], target = 9 → [0,1]

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

print(two_sum([2,7,11,15], 9))  # [0,1]
print(two_sum([3,2,4], 6))      # [1,2]
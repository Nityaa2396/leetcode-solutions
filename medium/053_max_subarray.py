# Problem 53: Maximum Subarray (Medium)
# Find the contiguous subarray with the largest sum
#
# Input: [-2,1,-3,4,-1,2,1,-5,4] → 6  (subarray [4,-1,2,1])
# Input: [1] → 1
# Input: [5,4,-1,7,8] → 23
#
# Approach: Kadane's algorithm — track current sum and max sum
# Time: O(n) | Space: O(1)

def max_subarray(nums):
    current = nums[0]
    best = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(max_subarray([1]))                         # 1
print(max_subarray([5,4,-1,7,8]))               # 23
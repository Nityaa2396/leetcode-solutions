# Problem 238: Product of Array Except Self (Medium)
# Return array where each element is product of all other elements
# Must solve without using division
#
# Input: [1,2,3,4] → [24,12,8,6]
# Input: [-1,1,0,-3,3] → [0,0,9,0,0]
#
# Approach: prefix products left to right, then suffix right to left
# Time: O(n) | Space: O(n)

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # left pass — result[i] = product of all elements to the left
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # right pass — multiply by product of all elements to the right
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

print(product_except_self([1,2,3,4]))       # [24,12,8,6]
print(product_except_self([-1,1,0,-3,3]))   # [0,0,9,0,0]
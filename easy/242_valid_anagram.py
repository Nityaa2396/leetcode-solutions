# Problem 242: Valid Anagram
# Given two strings s and t, return true if t is an anagram of s
# An anagram uses all the same characters in a different order
# Input: s = "anagram", t = "nagaram" → True
# Input: s = "rat", t = "car" → False

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    return True

print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
print(is_anagram("a", "ab"))             # False
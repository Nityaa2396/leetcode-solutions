# Problem 49: Group Anagrams (Medium)
# Given an array of strings, group the anagrams together.
# Two strings are anagrams if they contain the same characters.
#
# Example:
# Input:  ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
#
# Approach: Sort each word → use as dictionary key
# Time: O(n * k log k) where k = max word length
# Space: O(n)

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))  # "eat" → "aet", "tea" → "aet"
        anagrams[key].append(word)
    return list(anagrams.values())

# Test cases
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# [['eat','tea','ate'],['tan','nat'],['bat']]

print(groupAnagrams([""]))   # [['']]
print(groupAnagrams(["a"]))  # [['a']]
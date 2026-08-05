# Problem 125: Valid Palindrome
# A phrase is a palindrome if it reads the same forward and backward
# considering only alphanumeric characters, ignoring case
# Input: "A man, a plan, a canal: Panama" → True
# Input: "race a car" → False

def is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                       # False
print(is_palindrome(" "))                                # True
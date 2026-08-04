# Problem 20: Valid Parentheses
# Return true if brackets are correctly matched
# Input: "()" → True | "([)]" → False

def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_valid("()"))      # True
print(is_valid("()[]{}")), # True
print(is_valid("(]"))      # False
print(is_valid("{[]}"))    # True
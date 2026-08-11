# Problem 155: Min Stack (Medium)
# Design a stack that supports push, pop, top, and getMin in O(1)
#
# MinStack obj = MinStack()
# obj.push(-2); obj.push(0); obj.push(-3)
# obj.getMin() → -3
# obj.pop()
# obj.top()    → 0
# obj.getMin() → -2
#
# Approach: use two stacks — one normal, one tracking minimums
# Time: O(1) for all operations | Space: O(n)

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        # push to min_stack only if it's the new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

# Test
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())  # -3
obj.pop()
print(obj.top())     # 0
print(obj.getMin())  # -2
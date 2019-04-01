# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
    def size(self):
        return len(self.__items)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = Stack()
        max_len = 0
        tmp_len = 0
        new_substr = True
        for item in s:
            if item == '(':
                stack.push(item)
                new_substr = False
            elif item == ')':
                # print(tmp_len)
                p = stack.pop()
                if p == '(':
                    tmp_len += 2
                    max_len = tmp_len
                else:
                    new_substr = True
                    tmp_len = 0
        return max_len

s = Solution()
# print(s.longestValidParentheses("(()"))
# print(s.longestValidParentheses(")()())"))
print(s.longestValidParentheses("()(()"))
        

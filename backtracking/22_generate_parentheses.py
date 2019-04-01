# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
# For example, given n = 3, a solution set is:
# 
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def generateParenthesis(self, n : int) -> list:
        self.result = []
        self.backtrace('', 0, 0, n)
        return self.result

    def backtrace(self, s, open:int , close:int, max:int):
        if len(s) == max*2:
            self.result.append(s)
            return
        if open < max:
            self.backtrace(s+'(', open+1, close, max)
        if close < max and close < open:
            self.backtrace(s+')', open, close+1, max)

s = Solution()
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
print(s.generateParenthesis(4))

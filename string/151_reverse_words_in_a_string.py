# Given an input string, reverse the string word by word.
# 
# Example 1:
# 
# Input: "the sky is blue"
# Output: "blue is sky the"
# Example 2:
# 
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:
# 
# Input: "a good   example"
# Output: "example good a"

class Solution:
    def reverseWords(self, s: str) -> str:
        wlist = s.strip().split(' ')

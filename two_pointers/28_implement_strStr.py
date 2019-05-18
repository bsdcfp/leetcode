# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# 
# Example 1:
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
# 
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if needle:
      if not haystack:
         return -1
      for i in range(len(haystack)):
        if len(haystack)-i < len(needle):
          return -1
        n = 0
        while n < len(needle):
          if haystack[i+n] != needle[n]:
            break
          n += 1
        if n == len(needle):
          return i
      return -1
    else:
      return 0
s = Solution()
# print(s.strStr("a", "a"))
# print(s.strStr("hello", "ll"))
# print(s.strStr("aaaa", "bba"))
print(s.strStr("mississippi","a"))


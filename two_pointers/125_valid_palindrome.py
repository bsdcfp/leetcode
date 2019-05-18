# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# 
# Example 1:
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
# 
# Input: "race a car"
# Output: false
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
      if not s:
        return True
      s = re.sub(r'[^a-z0-9]*', '', s.lower())
      # s = re.sub(r'[a-z0-9]*', '', s.lower())
      left = 0
      right = len(s)-1
      while left <= right:
        if s[left] != s[right]:
          break
        left += 1
        right -= 1
      return True if left >= right else False

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
        

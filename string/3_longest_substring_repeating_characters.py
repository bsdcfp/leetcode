# Given a string, find the length of the longest substring without repeating characters.
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# Input: "abba"
# Output: 2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        strpos = {}
        max_len = 0
        start = 0
        for i in range(len(s)):
            start = strpos.get(s[i])+1 if strpos.get(s[i]) is not None and start < strpos.get(s[i])+1 else start
            strpos[s[i]] = i
            max_len = i-start+1 if i-start+1 > max_len else max_len
            # print(i, start, strpos, max_len)
        return max_len

s = Solution()
print(s.lengthOfLongestSubstring('bbbbb'))
print(s.lengthOfLongestSubstring('abcabcbb'))
print(s.lengthOfLongestSubstring('pwwkew'))
print(s.lengthOfLongestSubstring('abba'))


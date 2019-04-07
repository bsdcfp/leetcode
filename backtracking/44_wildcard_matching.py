# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
# 
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:
# 
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:
# 
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:
# 
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
import time
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        self.rec_matrix = [[ None for x in range(len(p))] for y in range(len(s))] # 已经检索过的索引，可以直接返回结果。避免回溯过深
        # print(self.rec_matrix)
        res = self._match(s, p, 0, 0)
        print(self.rec_matrix)
        return res

    def _match(self, text, pattern, si, pj):
        s = text[si:]
        p = pattern[pj:]
        print(s, p, si, pj)

        if not p:
            return not s

        if not s:
            return True if '*' == ''.join(list(set(p))) else False

        if (len(p) - p.count('*')) > len(s):
            return False
        
        if bool(p) and bool(s) and self.rec_matrix[si][pj] is not None:
            return self.rec_matrix[si][pj]

        if p[0] == '*':
            while pj+1 < len(pattern) and pattern[pj+1] == '*':
                pj += 1
            # self.rec_matrix[si][pj] = ( self._match(text, pattern, si, pj) or self._match(text, pattern, si+1, pj-1))
            self.rec_matrix[si][pj] = ( self._match(text, pattern, si, pj+1) or self._match(text, pattern, si+1, pj))
            return self.rec_matrix[si][pj]
        else:
            first_match = bool(s) and p[0] in {s[0], '?'}
            self.rec_matrix[si][pj] = ( first_match and self._match(text, pattern, si+1, pj+1))
            return self.rec_matrix[si][pj]
     
start = time.time()
s = Solution()
# print(s.isMatch("aa", "a"))
# print(s.isMatch("aa", "*"))
# print(s.isMatch("cb", "?a"))
# print(s.isMatch("adceb", "*a*b"))
# print(s.isMatch("acdcb", "*a*c?b"))
# print(s.isMatch("ababbabbbbbbbaaaaabaabb", "*b***ab*a"))
# print(s.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb","b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"))
# print(s.isMatch("aabbaabbbaabababaaababbabaaabbbbbbaababbabaababbabaaabbabbaabbaaaaaaaababbaabbbbbbababbaababbaabbabbaaaabaaaaaabbaaabaabbababbaabbbaababaaaaaabaababbaababbbabbabbabaaaaaaababbabbbababbbbbaaaabbaaaabaabb","b*a***baaaa*aba*b*b**bbb*b*b****b**a**a*aa*ab***ba*ababab****a*a*ba*aaaaa*abb*a*a**b***a*aaba*baab*ab*b"))
# print(s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b"))
print(s.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb","b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"))
print((time.time()-start))

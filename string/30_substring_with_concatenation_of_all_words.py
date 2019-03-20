# 30. Substring with Concatenation of All Words
# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
# 
# Example 1:
# 
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# Example 2:
# 
# Input:
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# Output: []

from itertools import combinations
from itertools import permutations
class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        res = []
        pattern_list = self._get_words_concatenation(words)
        for pattern in pattern_list:
            res += self._KMPMatch(s, pattern)
        print(list(set(res)))

    def _generate_pmt(self, string):
        """对模式串的字串，计算最大公共元素长度，获得最大长度表"""
        patterns = []
        for i in range(len(string)):
            patterns.append(string[0:i+1])
        # print(patterns)
        max_common = []
        for p in patterns:
            prefixs, suffixs = set([]), set([])
            size = len(p)
            for i in range(size-1):
                prefixs.add(p[0:i+1])
                suffixs.add(p[-i-1:])
            # print(prefixs, suffixs)
            max_common.append(self._get_max_len(prefixs & suffixs))
        return max_common 

    def _get_max_len(self, data: set) -> int:
        max_len = 0
        for s in data:
            if max_len < len(s):
                max_len = len(s) 
        return max_len 

    def _get_next(self, max_common):
        next = [-1]
        next.extend(max_common[0:-1])
        return next
    
    def _get_next_2(self, max_common):
        next = []
        for i in range(len(max_common)):
            print(i, i-max_common[i])
            next.append(i-max_common[i])
        return next
    
    def _KMPMatch(self, target, pattern):
        start, cur = 0, 0
        mres = []
        next = self._get_next(self._generate_pmt(pattern))
        for i in range(len(target)):
            for j in range(len(pattern)):
                if target[i] != pattern[j]:
                    i += next[j]
                    start = i
                    break
                if j == len(pattern)-1:
                    print(start)
                    mres.append(start)
                if i < len(target)-1:
                    i += 1
                    j += 1
        return mres

    def _get_words_concatenation(self, words):
        return [''.join(item) for item in list(permutations(words, len(words)))]

s = Solution()
# print(s._get_words_concatenation(["word","good","best","word"]))
# print(s._get_words_concatenation( ["foo","bar"]))
# print(s._generate_pmt('ABC'))
# print(s._generate_pmt('ABCD'))
# print(s._generate_pmt('ABCDA'))
# print(s._generate_pmt('ABCDABC'))
# print(s._get_next(s._generate_pmt('ABCDABD')))
# print(s._get_next_2(s._generate_pmt('ABCDABD')))
# s.findSubstring("barfoothefoobarman", ["foo","bar"])
# s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])
s._KMPMatch("barfoothefoobarman", "bar")

#   Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# 
#   A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# 
#   Input: "2"
#   Output: ["a", "b", "c"]

#   Input: "22"
#   Output: ["aa","ab","ac","ba","bb","bc","ca","cb","cc"]

#   Input: "23"
#   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

#   Input: "234"
#   Output:
#   ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi]

import itertools
PHONE_NUM = { 2: 'abc',
              3: 'def',
              4: 'ghi',
              5: 'jkl',
              6: 'mno',
              7: 'pqrs',
              8: 'tuv',
              9: 'wxyz'}

class Solution:
    def letterCombinations(self, digits: str) -> list:
        if len(digits) == 1:
            return list(map(str, PHONE_NUM[int(digits)]))
        pools = [tuple(PHONE_NUM[i]) for i in list(map(int, digits))]
        res = []
        for pool in pools:
            letters = list(map(str, pool))
            res = letters[:] if not res else list(self._get_combinations(res, letters))
        return res

    def _get_combinations(self, l1, l2):
        for x in l1:
            for y in l2:
                yield x+y
            


# print(list(map(str, itertools.combinations('ABCD', 3))))
s = Solution()
print(s.letterCombinations('2'))
print(s.letterCombinations('22'))
print(s.letterCombinations('23'))
print(s.letterCombinations('234'))
# print(s.letterCombinations('2345'))

import os

# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

ROMAN = {'M': 1000, 
         'CM': 900, 
         'D': 500, 
         'CD': 400, 
         'C': 100,
         'XC': 90,
         'L': 50,
         'XL': 40,
         'X': 10,
         'IX': 9,
         'V': 5, 
         'IV': 4, 
         'I': 1}
ROMAN_LIST = sorted(ROMAN.items(),key=lambda x:x[1], reverse=True)
class Solution:
    def intToRoman(self, num: int) -> str:
        if num > 3999:
            return ''
        res = []
        for r, d in ROMAN_LIST:
            while num >= d:
                print(num, d)
                res.append(r)
                num -= d
        return ''.join(res)

s = Solution()
print(s.intToRoman(58))
print(s.intToRoman(1987))

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
class Solution:
    def intToRoman(self, num: int) -> str:
        if num > 3999:
            return ''
        res = []
        for r, d in ROMAN.items():
            while num >= d:
                res.append(r)
                num -= d
        return ''.join(res)

    def get_digit_1(self, num: int) -> list:
        res = []
        while num:
            num , r = divmod(num, 10)
            res.append(r)
        res.reverse()
        return res

    def get_digit_2(self, num: int) -> list:
        res = []
        while num:
            res.append(num % 10)
            num = num // 10 # floor division
        res.reverse()
        return res

    def get_digit_3(self, num: int) -> list:
        return list(map(int, str(num)))


s = Solution()
print(s.get_digit_1(58))
print(s.get_digit_2(58))
print(s.get_digit_3(58))

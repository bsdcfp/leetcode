import os

class Solution:
    def strWithout3a3b(self, A, B):
        res = []
        if A < 3 and B < 3:
            return ''.ljust(A, 'a') + ''.ljust(B, 'b') 
        else:
            idx = 0
            res = ''
            count = 0
            if A < B:
                while idx < A:
                    idx += 1
                    if idx  < B-A:
                        res += 'bba'
                        count += 2
                    else:
                        res += 'ba'
                        count += 1
                if count < B:
                    res += ''.ljust(B-count, 'b')
            elif A > B:
                while idx < B:
                    idx += 1
                    if idx  < A-B :
                        res += 'aab'
                        count += 2
                    else:
                        res += 'ab'
                        count += 1
                if count < A:
                    res += ''.ljust(A-count, 'a')
            else:
                while idx < B:
                    idx += 1
                    res += 'ab'
            return res

S = Solution()
print(S.strWithout3a3b(4,3))
print(S.strWithout3a3b(4,4))
print(S.strWithout3a3b(4,5))
print(S.strWithout3a3b(4,6))
print(S.strWithout3a3b(4,7))
print(S.strWithout3a3b(4,8))


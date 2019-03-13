import os, re, sys
INT_MAX = 2**31-1
INT_MIN = -2**31
print(INT_MAX)
print(INT_MIN)
class Str2Int(object):
    def atoi(self, str: str) -> int:
        pattern = re.compile(r'^(-|\+| +|)+[0-9]+')
        # num =  pattern.search(str)
        num = re.match(r'^(-|\+)?[0-9]+', str.strip())
        if num:
            num = int(num.group().strip('+'))
            if num < INT_MIN:
                return INT_MIN
            elif num > INT_MAX:
                return INT_MAX
            else:
                return num
        else:
            return 0

x = Str2Int()
print(x.atoi('  -89'))
print(x.atoi('4193 with words'))
print(x.atoi('-91283472332'))
print(x.atoi('42'))
print(x.atoi('words and 987'))
print(x.atoi('+-2'))

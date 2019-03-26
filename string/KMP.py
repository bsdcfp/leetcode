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
        if not s or not words:
            return res
        # pattern_list = self._get_words_concatenation(words)
        for pattern in self._get_words_concatenation(words):
            # print(pattern)
            # continue
            res += self._KMPMatch(s, pattern)
        return list(set(res))

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
        next = []
        if not max_common:
            return next
        next.append(1)
        for i in range(1, len(max_common)):
            next.append(i-max_common[i-1] if (i-max_common[i-1]) > 0 else 1)
        return next
    
    def _KMPMatch(self, target, pattern):
        start = 0
        mres = []
        next = self._get_next(self._generate_pmt(pattern))
        # print(next, self._generate_pmt(pattern))
        i = 0
        while i < len(target):
            if i == len(target):
                break
            j = 0
            while j < len(pattern):
                # print(i,j,start, pattern)
                if target[i] != pattern[j]:
                    start = start + next[j]
                    i = start
                    break
                if j == len(pattern)-1:
                    # print(i,j)
                    mres.append(start)
                    # start = i+1
                    start = start + next[j]
                    i = start
                    break
                i += 1
                j += 1
                if i == len(target) or j == len(pattern):
                    break
        # print(target, pattern, mres)
        return mres

    def _get_words_concatenation(self, words):
        for item in permutations(words, len(words)):
            yield ''.join(item)

s = Solution()
print(s.findSubstring("pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel",
    ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]))
# print(s.findSubstring("barfoothefoobarman", ["foo","bar"])) # [0, 9]
# print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])) # []
# print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])) # [6, 9, 12]
# print(s.findSubstring("a", ["a", "a"])) # []
# print(s.findSubstring("aaa", ["a", "a"])) # [0, 1]
# print(s.findSubstring("", [])) # []
# print(s.findSubstring("a", [])) # []
# print(s._KMPMatch("barfoothefoobarman", "barfoo"))
# print(s._KMPMatch("barfoothefoobarman", "bar"))
# print(s._KMPMatch("a", "aa"))
# print(s._KMPMatch("barfoofoobarthefoobarman", "foobarthe"))
# print(s._KMPMatch("barfoofoobarthefoobarman", "barthefoo"))

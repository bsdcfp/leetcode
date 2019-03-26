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

class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        res = []
        if not s or not words or not words[0]:
            return res
        step_len = len(words[0])
        words_dict = self._words_count(words)
        total_len = step_len*len(words)
        for i in range(len(s)):
            # print(i)
            target = s[i:i+total_len]
            if len(target) < total_len:
                break
            if self._split_match(target, words_dict, step_len):
                res.append(i)
        return res

    def _words_count(self, words):
        wdict = {}
        for w in words:
            if w in wdict:
                wdict[w] += 1
            else:
                wdict[w] = 1
        return wdict

    def _split_match(self, target, words_dict, step_len):
        tmp = {}
        tmp.update(words_dict)
        for i in range(0, len(target), step_len):
            word = target[i:i+step_len]
            if word not in tmp:
                return False
            else:
                count = tmp.get(word)
                if count-1:
                    tmp[word] = count -1
                else:
                    tmp.pop(word)
        # print(count, target, tmp)
        return True if not tmp else False
            


s = Solution()
print(s.findSubstring("pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel", ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]))
# print(s.findSubstring("barfoothefoobarman", ["foo","bar"])) # [0, 9]
# print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])) # []
# print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])) # [6, 9, 12]
# print(s.findSubstring("a", ["a", "a"])) # []
# print(s.findSubstring("aaa", ["a", "a"])) # [0, 1]
# print(s.findSubstring("", [])) # []
# print(s.findSubstring("a", [])) # []

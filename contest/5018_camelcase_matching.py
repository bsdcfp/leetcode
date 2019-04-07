# A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)
# 
# Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.
# Example 1:
# 
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
# Output: [true,false,true,true,false]
# Explanation: 
# "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
# "FootBall" can be generated like this "F" + "oot" + "B" + "all".
# "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
# Example 2:
# 
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
# Output: [true,false,true,false,false]
# Explanation: 
# "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
# "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
# Example 3:
# 
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
# Output: [false,true,false,false,false]
# Explanation: 
# "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".

import re

class Solution:
  def camelMatch(self, queries: list, pattern: str) -> list:
    self.res = []
    for query in queries:
      self.res.append(self._match(query, pattern))
    return self.res

  def _match(self, query, pattern):
    pattern_list = self._get_pattern_list(pattern)
    # print(pattern_list)
    elem_count = {} #记录每个大写字母之间子串的字符个数
    for i in range(len(query)):
      if re.match('[A-Z]', query[i]):
        if not pattern_list:
          return False
        if elem_count:
          p = pattern_list[0]
          # print(elem_count, p)
          if not elem_count.get('upper_case') and re.match('[A-Z]', p[0]):
            elem_count = {}
            elem_count[query[i]] = 1
            elem_count['upper_case'] = True
          else:
            for e in p:
              if not elem_count.get(e):
                return False
              elem_count[e] -= 1
              if elem_count[e] == 0:
                elem_count.pop(e)
            elem_count = {}
            elem_count[query[i]] = 1
            elem_count['upper_case'] = True
            pattern_list.pop(0)
        else:
          elem_count[query[i]] = 1
          elem_count['upper_case'] = True
      else:
          if elem_count.get(query[i]):
            elem_count[query[i]] += 1
          else:
            elem_count[query[i]] = 1
    # 处理query里的最后一个大写字母及其后的字串
    if elem_count:
      if not pattern_list:
        return False
      p = pattern_list.pop(0)
      # print(elem_count, p)
      for e in p:
        if not elem_count.get(e):
          return False
        elem_count[e] -= 1
        if elem_count[e] == 0:
          elem_count.pop(e)
    return True if not pattern_list else False
      
  def _get_pattern_list(self, pattern):
    pattern_list = []
    idx = 0
    for i in range(len(pattern)):
      if re.match('[A-Z]', pattern[i]):
        if pattern[idx:i]:
          pattern_list.append(pattern[idx:i])
        idx = i
        continue
    if idx <= len(pattern)-1:
      pattern_list.append(pattern[idx:])
    return pattern_list

s = Solution()
# print(s._get_pattern_list("FB"))
# print(s._get_pattern_list("FoBa"))
# print(s._get_pattern_list("FoBaT"))
print(s.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"))
print(s.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa"))
print(s.camelMatch( ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT"))
print(s.camelMatch(["CompetitiveProgramming","CounterPick","ControlPanel"], "CooP"))
print(s.camelMatch(["uAxaqlzahfialcezsLfj","cAqlzyahaslccezssLfj","AqlezahjarflcezshLfj","AqlzofahaplcejuzsLfj","tAqlzahavslcezsLwzfj","AqlzahalcerrzsLpfonj","AqlzahalceaczdsosLfj","eAqlzbxahalcezelsLfj"], "AqlzahalcezsLfj"))
print(s.camelMatch(["aksvbjLiknuTzqon","ksvjLimflkpnTzqn","mmkasvjLiknTxzqn","ksvjLiurknTzzqbn","ksvsjLctikgnTzqn","knzsvzjLiknTszqn"],"ksvjLiknTzqn"))
# print(s._match("FooBar", "FoBa"))
# print(s._match("FooBar", "FoBaT"))
# print(s._match("ControlPanel", "CooP"))
# print(s._match("uAxaqlzahfialcezsLfj", "AqlzahalcezsLfj"))
# print(s._match("aksvbjLiknuTzqon", "ksvjLiknTzqn"))

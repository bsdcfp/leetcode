# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of times.
# 
# Note:
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
# 
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
class Solution:
  def combinationSum(self, candidates: list, target: int) -> list:
    self.res = set([])
    for c in candidates:
      cur_sum = [] # 第一个元素表示所有元素的和
      cur_sum.append(c)
      cur_sum.append(c)
      self._calculate(candidates, target, cur_sum)
    print(list(map(lambda x: eval(x), self.res)))

  def _calculate(self, candidates, target, cur_sum):
    for c in candidates:
      new_sum = []
      new_sum.extend(cur_sum)
      # print(new_sum , c)
      if new_sum[0] == target:
        # sorted(new_sum, reverse=True)
        new_sum.sort(reverse=True)
        self.res.add(str(new_sum[1:]))
      elif (new_sum[0]+c) == target:
        # print(new_sum, target)
        new_sum.append(c)
        new_sum[0] += c
        print(new_sum, 'before')
        new_sum.sort(reverse=True)
        print(new_sum, 'after')
        self.res.add(str(new_sum[1:]))
      elif (new_sum[0]+c) < target:
        new_sum[0] += c
        new_sum.append(c)
        self._calculate(candidates, target, new_sum)

s = Solution()
# s.combinationSum([2,3,6,7], 7)
s.combinationSum([2,3,5], 8)
        

        

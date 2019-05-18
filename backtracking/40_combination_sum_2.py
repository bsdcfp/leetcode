# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
class Solution:
  def combinationSum2(self, candidates: list, target: int) -> list:
    self.res = set([])
    for i in range(len(candidates)):
      cum=[candidates[i]]
      cum.append(candidates[i])
      if cum[0] == target:
        self.res.add(str(sorted(cum[1:])))
      # new_candidates = []
      # new_candidates.extend(candidates)
      # new_candidates.pop(i)
      # print(new_candidates, cum)
      if i+1 < len(candidates):
        self._calculate(candidates[i+1:], target, cum) 
    print(list(map(lambda x: eval(x), self.res)))
    return list(map(lambda x: eval(x), self.res))

  def _calculate(self, candidates, target, cur_sum):
    for i in range(len(candidates)):
      new_sum = []
      new_sum.extend(cur_sum)
      total_sum = new_sum[0]
      # print(new_sum, candidates[i])
      # if total_sum == target:
      #   self.res.add(str(sorted(new_sum[1:])))
      if total_sum + candidates[i] == target:
        # print(new_sum, candidates[i])
        new_sum[0] += candidates[i]
        new_sum.append(candidates[i])
        self.res.add(str(sorted(new_sum[1:])))
      elif total_sum + candidates[i] < target:
        new_sum[0] += candidates[i]
        new_sum.append(candidates[i])
        # print(new_sum, candidates[i])
        if i+1 < len(candidates):
          new_candidates = candidates[i+1:]
          self._calculate(new_candidates, target, new_sum)

s = Solution()
s.combinationSum2([2,5,2,1,2], 5)
s.combinationSum2([10,1,2,7,6,1,5], 8)
s.combinationSum2([1], 1)

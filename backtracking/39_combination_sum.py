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
    self.res = []
    self._calculate(candidates, target, 0)
    print(self.res)
  def _calculate(self, candidates, target, cur_sum):
    for c in candidates:
      # cur_sum += c
      if (cur_sum+c) == target:
        self.res.append(cur_sum+c)
      elif (cur_sum+c) < target:
        self._calculate(candidates, target, cur_sum+c)

s = Solution()
s.combinationSum( [2,3,6,7], 7)
        

        

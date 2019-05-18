# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
class Solution:
  def permute(self, nums: list) -> list:
    self.res = []
    prmts = []
    self._permute(nums, prmts)
    return self.res
  def _permute(self, nums, prmts):
    # print(nums, prmts)
    for i in range(len(nums)):
      new_prmts = prmts[:]
      remain_nums = nums[:]
      n = remain_nums.pop(i)
      new_prmts.append(n)
      if not remain_nums:
        self.res.append(new_prmts)
      else:
        self._permute(remain_nums, new_prmts)
   

s = Solution()
# print(s.permute([1, 2, 3]))
# print(s.permute([1]))
# print(s.permute([]))
print(s.permute([1, 1, 2]))

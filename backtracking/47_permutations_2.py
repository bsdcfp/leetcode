# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# 
# Example:
# 
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
class Solution:
  def permuteUnique(self, nums: list) -> list:
    self.res = set([])
    prmts = []
    self._permute(nums, prmts)
    return list(map(lambda x: eval(x), self.res))
  def _permute(self, nums, prmts):
    # print(nums, prmts)
    for i in range(len(nums)):
      new_prmts = prmts[:]
      remain_nums = nums[:]
      n = remain_nums.pop(i)
      new_prmts.append(n)
      if not remain_nums:
        self.res.add(str(new_prmts))
      else:
        self._permute(remain_nums, new_prmts)
   

s = Solution()
# print(s.permute([1, 2, 3]))
# print(s.permute([1]))
# print(s.permute([]))
print(s.permuteUnique([1, 1, 2]))

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
  def __init__(self):
    self.num_idx = {}

  def put(self, n):
    if n in self.num_idx:
      self.num_idx[n] += 1
    else:
      self.num_idx[n] = 1

  def pop(self, n):
    if self.num_idx and n in self.num_idx:
      self.num_idx[n] -= 1
      if self.num_idx[n] == 0:
        self.num_idx.pop(n)

  def threeSum(self, nums: list) -> list:
    if not nums:
      return []
    nums.sort()

    # for n in nums:
    #   if n in self.num_idx:
    #     self.num_idx[n] += 1
    #   else:
    #     self.num_idx[n] = 1

    res = set([])
    for i in range(len(nums)-2):
      sum=-nums[i]
      lo = i+1
      hi = len(nums)-1
      while lo < hi:
        if (nums[lo] + nums[hi]) == sum:
          res.add(str([nums[i], nums[lo], nums[hi]]))
          while lo < hi and nums[lo] == nums[lo+1]: lo += 1
          while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
          hi -= 1 
          lo += 1
        elif (nums[lo] + nums[hi]) < sum:
          lo += 1
        else:
          hi -= 1
        
    return list(map(lambda x: eval(x), res))

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
  

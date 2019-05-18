# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
class Solution:
  # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
  def fourSum(self, nums: list, target: int) -> list:
    res = set([])
    if not nums or len(nums) < 4:
      return 
    nums.sort()
    for i in range(len(nums)-3):
      for j in range(i+1, len(nums)-2):
        lo = j+1
        hi = len(nums)-1
        while lo < hi:
          sum = nums[i]+nums[j]+nums[lo]+nums[hi]
          if sum == target:
            res.add(str([nums[i],nums[j],nums[lo],nums[hi]]))
            while lo < hi and nums[lo] == nums[lo+1]: lo += 1
            while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
            lo += 1
            hi -= 1
          elif sum < target:
            lo += 1
          else:
            hi -= 1
    return list(map(lambda x: eval(x), res))

s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
 

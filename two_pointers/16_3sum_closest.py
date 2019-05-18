# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
class Solution:
  # def threeSumClosest(self, nums: List[int], target: int) -> int:
  def threeSumClosest(self, nums: list, target: int) -> int:
    if not nums:
      return
    nums.sort()
    closest = 1000000
    for i in range(len(nums)-2):
      lo = i+1
      hi = len(nums)-1
      while lo < hi:
        sum = nums[lo]+nums[hi]+nums[i]
        if sum == target:
          return target
        elif sum < target:
          lo += 1
        else:
          hi -= 1
        if self.distance(sum, target) < self.distance(closest, target):
          closest = sum
    return closest

  def distance(self, num1, num2):
    return (num1-num2) if num1 > num2 else (num2-num1)

s = Solution()
print(s.threeSumClosest( [-1, 2, 1, -4], 1))
print(s.threeSumClosest( [-1, 2, 1, -4], 2))
print(s.threeSumClosest( [-1, 2, 1, -4], -3))

# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this problem.
# 
# Example:
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:
# 
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
class Solution:
  def sortColors(self, nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if not nums:
      return
    # 三个指针，索引红黄蓝三种颜色的位置
    lo = 0
    mid = 0
    hi = len(nums)-1
    while mid <= hi:
      print(lo, mid, hi, nums)
      if nums[mid] == 0:
        if nums[lo] > 0:
          self.swap(nums, lo, mid)
        lo += 1
      elif nums[mid] == 2:
        if nums[hi] < 2:
          self.swap(nums, hi, mid)
        hi -= 1
      else:
        mid += 1
      if mid < lo:
        mid = lo

        
    print(nums)

  def swap(self, nums, idx1, idx2):
    tmp = nums[idx1]
    nums[idx1] = nums[idx2]
    nums[idx2] = tmp

s = Solution()
s.sortColors([2,0,1])
# s.sortColors([2,0,2,1,1,0])

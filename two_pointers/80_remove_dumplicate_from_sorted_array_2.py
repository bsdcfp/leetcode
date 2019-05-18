# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# 
# Example 1:
# 
# Given nums = [1,1,1,2,2,3],
# 
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# 
# It doesn't matter what you leave beyond the returned length.

# Example 2:
# 
# Given nums = [0,0,1,1,1,1,2,3,3],
# 
# Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
# 
# It doesn't matter what values are set beyond the returned length.
class Solution:
  def removeDuplicates(self, nums: list) -> int:
    if not nums:
      return 0
    if len(nums) == 1:
      return 1
    fst = -1
    sec = -1 
    count = 0
    # print(nums)
    while fst < len(nums)-1:
      fst += 1
      if sec < 0 and count == 2:
        sec = fst

      if nums[fst] == nums[fst-1]:
        count += 1
      elif nums[fst] != nums[fst-1]:
        count = 1

      if sec > 0 and count <= 2:
        nums[sec] = nums[fst]
        sec += 1

    # print(nums)
    return sec if sec > 0 else len(nums)

s = Solution()
# print(s.removeDuplicates([1,1,1,2,2,3,3,3]))
# print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))
print(s.removeDuplicates([1]))
print(s.removeDuplicates([1, 2]))

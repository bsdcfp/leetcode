# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# 
# Note:
# 
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
class Solution:
  def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    lo = m-1
    hi = m+n-1
    ano = n-1
    while ano >= 0:
      if lo < 0:
        nums1[hi] = nums2[ano]
        hi -= 1
        ano -= 1
        continue
      if nums2[ano] >= nums1[lo]:
        nums1[hi] = nums2[ano]
        hi -= 1
        ano -= 1
      else:
        nums1[hi] = nums1[lo]
        lo -= 1
        hi -= 1
    print(nums1)
    
s = Solution()
s.merge([1,2,3,0,0,0], 3, [2,5,6], 3) 

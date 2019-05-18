# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
# 
# Example:
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
class Solution:
  def trap(self, height: list) -> int:
    if not height or len(height) < 3:
      return 0
    lo = 0
    hi = len(height)-1
    area = 0
    lo_max = 0
    hi_max = 0
    while lo < hi:
      if height[lo] < height[hi]:
        if height[lo] < lo_max:
          area += lo_max-height[lo]
        else:
          lo_max = height[lo]
        lo += 1
      else:
        if height[hi] < hi_max:
          area += hi_max-height[hi]
        else:
          hi_max = height[hi]
        hi -= 1
    return area

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([2,1,2,1]))
print(s.trap([4,2,3]))

        

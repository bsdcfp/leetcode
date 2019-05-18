# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
# 
# For example,
# [2,3,4], the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
#  
# 
# Example:
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
import heapq
class MedianFinder:
  def __init__(self):
    """
    initialize your data structure here.
    """
    self.small_max = []
    self.large_min = []

  def addNum(self, num: int) -> None:
    heapq.heappush(self.small_max, -heapq.heappushpop(self.large_min, num))
    if len(self.small_max) < len(self.large_min):
      heapq.heappush(self.small_max, -heapq.heappop(self.large_min))

  def findMedian(self) -> float:
    return -self.small_max[0] if len(self.small_max) > len(self.large_min) else (large_min[0]-small_max[0])/2
        


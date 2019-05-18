# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# 
# Example 2:
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import random
class Solution:
  def merge(self, intervals: list) -> list:
    if not intervals or len(intervals) == 1 :
      return intervals 
    self._quicksort(intervals)
    # print(intervals)
    self.res = []
    for interval in intervals:
      # if not self.res or self.res[-1].end < interval.start:
      if not self.res or self.res[-1][1] < interval[0] :
        self.res.append(interval)
      # self.res[-1].end = interval.end
      elif self.res[-1][1] < interval[1]:
        self.res[-1][1] = interval[1]
    print(self.res)
    return self.res
    # print(intervals)

  def _quicksort(self, intervals, left=None, right=None):
    if left is None or right is None:
      left = 0
      right = len(intervals)-1
    if left >= right:
      return
    pivot_pos = self._partition(intervals, left, right)
    # print(pivot_pos)
    self._quicksort(intervals, left, pivot_pos-1)
    self._quicksort(intervals, pivot_pos+1, right)

  def _partition(self, intervals, left, right):
    pivot = random.randint(left, right)
    print(left, right, pivot)
    # 将游标放到最后
    if pivot != right:
      self._swap(intervals, pivot, right)
      pivot = right
    # 定义索引
    i = 0
    j = right-1
    while i<right:
      # print(i, j)
      # if intervals[i].start >= intervals[pivot].start:
      if intervals[i][0] > intervals[pivot][0]:
        if j < i:
          break
        # elif j >= i and intervals[j].start < intervals[pivot].start:
        elif j >= i and intervals[j][0] < intervals[pivot][0]:
          self._swap(intervals, i, j)
          i += 1
        else:
          j -= 1
      else:
        i += 1
    self._swap(intervals, i, pivot)
    return i

  def _swap(self, intervals, idx1, idx2):
    tmp = intervals[idx1]
    intervals[idx1] = intervals[idx2]
    intervals[idx2] = tmp

s = Solution()
# s.merge([[2, 7],[3, 4], [9, 11],[1,3],[9,16],[8,10],[5,18]])
# s.merge([[1,4],[1,5]])
s.merge([[1,3],[2,6],[8,10],[15,18]])
# s.merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]])
# s._quicksort([[2, 7],[3, 4], [9, 11],[1,3],[9,16],[8,10],[5,18]])

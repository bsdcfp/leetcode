# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the two partitions.
# 
# Example:
# 
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import sys
class Solution:
  def partition(self, head: ListNode, x: int) -> ListNode:
    dummy = ListNode(-sys.maxsize-1)
    dummy.next = head
    first = dummy
    second = dummy
    while first.next:
      if first.val < x and first.next.val >= x:
        second = first
        first = first.next
      elif first.val >= x and first.next.val < x:
        tmp = second.next
        second.next = first.next
        first.next = first.next.next
        second.next.next = tmp
    return dummy.next
        

# Given a linked list, remove the n-th node from the end of list and return its head.
# 
# Example:
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
      first = head
      second = head
      list_len = 0
      while first:
        list_len += 1
        first = first.next
      if list_len < 2:
        return 
      idx = list_len-n-1
      if idx < 0:
        head = head.next
        return head
      while idx > 0:
        second = second.next
        idx -= 1
      second.next = second.next.next
      return head
  def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
    if not head:
      return
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    length = 0
    while first and length != n+1:
      first = first.next
      length += 1 
    while first:
      first = first.next
      second = second.next
    second.next = second.next.next
    return dummy.next

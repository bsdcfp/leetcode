# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  def inorderTraversal(self, root: TreeNode) -> list:
    res = []
    stack = []
    node = root
    while node or stack:
      while node:
        stack.append(node)
        node = node.left
      node = stack.pop(len(stack)-1)
      res.append(node.val)
      node = node.right
    return res

        
    
    
        

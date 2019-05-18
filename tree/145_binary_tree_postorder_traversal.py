# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  def postorderTraversal(self, root: TreeNode) -> list:
    res = []
    stack = []
    node = root
    while node or stack:
      if node:
        stack.append(node)
        res.insert(0, node.val)
        node = node.right
      else:
        node = stack.pop(-1)
        node = node.left
        
    return res

        
    
    
        

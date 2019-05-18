# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def levelOrder(self, root: TreeNode) -> List[List[int]]:
    res = []
    level_res = []
    stack_level_up = []
    stack_level_down = []
    stack_level_up.append(root)
    while stack_level_up:
      node = stack_level_up.pop(0)
      if node:
        level_res.append(node.val)
        # print(node.val, len(stack_level_up), len(stack_level_down))
        if node.left: stack_level_down.append(node.left)
        if node.right: stack_level_down.append(node.right)
      if not stack_level_up:
        if level_res:
          res.append(level_res)
          level_res = []
        if stack_level_down:
          stack_level_up.extend(stack_level_down)
          stack_level_down = []
    return res
        
    
 

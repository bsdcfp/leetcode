import os

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


import copy
class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        if not root:
            return False 
        q = []
        q.append(root)
        while q:
            level = []
            value = []
            for i in range(len(q)):
                TreeNode node = q.pop(0)
                if node.left:
                    level.append(node.left)
                    value.append(node.left.value)
                if node.right:
                    level.append(node.right)
                    value.append(node.right.value)
            if x in value and y in value:
                return True
            else:
                q = copy.deepcopy(level)
        return False




        pass

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        levels = collections.defaultdict(list)

        def search(root, level):
            if root is None:
                return
            levels[level].append(root.val)
            search(root.left, level + 1)
            search(root.right, level + 1)

        search(root, 0)
        
        max_level = max(levels.keys())
        
        for level in range(max_level + 1):
            vals = levels[level]
            if level % 2 == 0:
                if vals[0] % 2 == 0 or vals[-1] % 2 == 0:
                    return False
                for i in range(len(vals)-1):
                    if vals[i] % 2 == 0:
                        return False
                    if vals[i] >= vals[i+1]:
                        return False                
            else:
                if vals[0] % 2 == 1 or vals[-1] % 2 == 1:
                    return False
                for i in range(len(vals)-1):
                    if vals[i] % 2 == 1:
                        return False
                    if vals[i] <= vals[i+1]:
                        return False
        return True
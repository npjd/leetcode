# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth_helper(root, depth):
            if root is None:
                return depth
            return max( depth_helper(root.left, depth +1), depth_helper(root.right, depth +1))
        
        return depth_helper(root, 0)
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inorder(root, lst):
            if root is None:
                return
            inorder(root.left, lst)
            lst.append(root.val)
            inorder(root.right, lst)
            return lst
        
        return inorder(root, [])
            
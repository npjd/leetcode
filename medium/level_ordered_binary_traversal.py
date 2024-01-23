from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque([root])

        ans = []

        while len(q) != 0:
            curr_level = []

            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node.val)

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            ans.append(curr_level)

        return ans
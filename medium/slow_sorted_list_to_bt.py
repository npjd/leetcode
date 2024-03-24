# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next
        
        
        def recurse(start, end):
            if start > end:
                return None
            n = end + start
            mid = n // 2
            return TreeNode(array[mid], recurse(start, mid-1), recurse(mid+1, end))
        
        return recurse(0, len(array)-1)
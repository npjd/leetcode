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
        
        def get_middle(head):
            prev = None
            slow_ptr = head
            fast_ptr = head

            while fast_ptr and fast_ptr.next:
                prev = slow_ptr
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            
            if prev:
                prev.next = None

            return slow_ptr
        
        mid = get_middle(head)

        tree = TreeNode(mid.val)
        if head == mid:
            left_tree = None
        else:
            left_tree = self.sortedListToBST(head)
        right_tree = self.sortedListToBST(mid.next)

        tree.left = left_tree
        tree.right = right_tree

        return tree
        
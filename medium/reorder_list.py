# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if head is None or head.next is None:
            return
        
        s = head
        f = head
        prev = None
        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next
        
        prev.next = None


        second = None
        while s is not None:
            tmp = s.next
            s.next = second
            second = s
            s = tmp

        first = head
        second = second

        while head is not None:
            tmp1 = head.next
            tmp2 = second.next

            head.next = second

            # if dont make second.next tmp1 if we at the end, either second is none or has our last element
            if tmp1 is None:
                break

            second.next = tmp1


            head = tmp1
            second = tmp2

        
        

        
        


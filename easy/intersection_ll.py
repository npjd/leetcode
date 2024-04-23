class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        lenA = 0
        lenB = 0

        tempA = headA
        tempB = headB

        while tempA != None:
            lenA += 1
            tempA = tempA.next
    
        while tempB != None:
            lenB += 1
            tempB = tempB.next
        
        diff = abs(lenA - lenB)

        if lenA > lenB:
            for _ in range(diff):
                tmp = headB
                headB = ListNode(0)
                headB.next = tmp
        elif lenB > lenA:
            for _ in range(diff):
                tmp = headA
                headA = ListNode(0)
                headA.next = tmp
       
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
        
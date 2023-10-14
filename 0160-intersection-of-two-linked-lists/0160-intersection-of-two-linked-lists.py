# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        setA = set()
        curr = headA
        while curr:
            setA.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in setA:
                break
            curr = curr.next
        return curr
        
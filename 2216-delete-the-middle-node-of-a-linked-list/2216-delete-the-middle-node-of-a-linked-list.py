# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        if not head.next.next:
            head.next = None
            return head
        fast = head.next.next
        prev = head
        while fast and fast.next:
            fast = fast.next.next
            prev = prev.next
        prev.next = prev.next.next
        return head
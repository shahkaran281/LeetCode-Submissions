# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and head.next == None:
            return None
        i = 1
        first = head
        while i < n and first != None:
            first = first.next
            i+=1
        last = head
        prev = head
        while first.next != None:
            first = first.next
            prev = last
            last = last.next
        if last == prev:
            head = head.next
        else:
            prev.next = last.next
        return head

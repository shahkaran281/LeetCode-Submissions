# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        last = None
        first = head
        sec = head.next
        while first and sec:
            if last == None:
                head = sec
            else:
                last.next = sec
            nxt = sec.next
            sec.next = first
            first.next = nxt
            last = first
            # print("Before,Last:",last)
            first = first.next
            if first:
                sec = first.next
            # print("After,Last:",last)

        return head
        
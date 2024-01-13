# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappush, heappop 

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        heap = []
        heapify(heap)
        for list in lists:
            curr = list
            while curr:
                heappush(heap,curr.val)
                curr = curr.next
        if not heap:
            return None
        head = ListNode(heappop(heap),None)
        prev = head
        while heap:
            curr = ListNode(heappop(heap),None)
            prev.next = curr
            prev = curr
        return head

        
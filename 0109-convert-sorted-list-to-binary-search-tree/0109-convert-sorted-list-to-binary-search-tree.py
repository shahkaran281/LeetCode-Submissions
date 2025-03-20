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
        if not head:
            return None
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        def fun(i,j):
            if i > j:
                return None
            mid = (i+j) // 2
            # print(i,mid,j)
            node = TreeNode(arr[mid])
            node.left = fun(i,mid-1)
            node.right = fun(mid+1,j)
            return node
        return fun(0,len(arr)-1)
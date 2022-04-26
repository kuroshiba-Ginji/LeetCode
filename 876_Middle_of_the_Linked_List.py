# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        N = 1
        cur = head
        while cur.next != None:
            N += 1
            cur = cur.next

        target = N//2+1

        cur = head
        i = 1

        while cur.next != None:
            if i == target:
                return cur
            cur = cur.next
            i += 1
        return cur

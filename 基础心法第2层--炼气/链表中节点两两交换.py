# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return self.next


import time

#  Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
# print(node1.next.next.next.val)

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
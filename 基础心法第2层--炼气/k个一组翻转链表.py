import time

#  Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 1
        cur = head
        re_cur = head
        while cur:
            cur = cur.next
            count += 1
            if count % k == 0:
                tmp, cur.next = cur.next, None 
                re_tmp = self.reverse(re_cur)
                re_cur = tmp

    def reverse(self, head)
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, cur = None, head
        while cur:
            cur, pre, cur.next = cur.next, cur, pre
        return cur
# Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
# Example 1
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# Example 2
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

from typing import Optional, Union


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            for _ in range(k):
                pre, cur = cur, cur.next
                if not cur:
                    return dummy.next
            pre.next = self.reverse(cur, k)
            cur = pre.next
        return dummy.next

    def reverse(self, head: ListNode, k: int) -> Optional[ListNode]:
        pre, cur = None, head
        for _ in range(k):
            cur.next, cur, pre = pre, cur.next, cur
        return cur

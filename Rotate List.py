# Rotate List
# Given the head of a linked list, rotate the list to the right by k places.
# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head
        k %= length
        for _ in range(length - k):
            cur = cur.next
        res = cur.next
        cur.next = None
        return res

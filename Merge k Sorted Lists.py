# Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy = ListNode(0)
        cur = dummy
        while True:
            min_index = -1
            min_val = float("inf")
            for i, node in enumerate(lists):
                if node and node.val < min_val:
                    min_index = i
                    min_val = node.val
            if min_index == -1:
                break
            cur.next = ListNode(min_val)
            cur = cur.next
            lists[min_index] = lists[min_index].next
        return dummy.next

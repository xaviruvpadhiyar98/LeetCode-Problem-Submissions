# Partition List
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        dummy_left = ListNode(0)
        dummy_right = ListNode(0)
        left = dummy_left
        right = dummy_right
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        right.next = None
        left.next = dummy_right.next
        return dummy_left.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    r = s.partition(head, 3)
    while r:
        print(r.val)
        r = r.next

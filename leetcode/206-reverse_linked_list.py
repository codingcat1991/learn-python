# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        prev = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        head = prev
        return head

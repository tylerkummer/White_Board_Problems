# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        last = 0
        head = prev = None
        while True:
            if l2 is None and l1 is None and last == 0:
                break
            val = last
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if val >= 10:
                val = val % 10
                last = 1
            else:
                last = 0
            current = ListNode(val)
            if prev is None:
                head = current
            else:
                prev.next = current
            prev = current
        return head

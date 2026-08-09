# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        newHead = ListNode(stack[-1])
        curr = newHead
        for v in reversed(stack[:-1]):
            temp = ListNode(v)
            curr.next = temp
            curr = curr.next
        return newHead
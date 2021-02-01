class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []

        ans = ListNode(0)
        node = ans

        while head:
            stack.append(head.val)
            head = head.next

        while stack:
            node.next = ListNode(stack.pop())
            node = node.next

        return ans.next

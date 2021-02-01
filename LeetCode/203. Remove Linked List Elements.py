class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = None
        ret = None
        while head:
            if head.val != val:
                if node:
                    node.next = ListNode(head.val)
                    node = node.next
                else:
                    node = ListNode(head.val)
                    ret = node
            head = head.next

        return ret

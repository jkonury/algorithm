class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        start = 1
        new_head = None
        reverse_node = None
        ret = None

        while head:
            if m <= start <= n:
                node = head
                head = head.next
                node.next = reverse_node
                reverse_node = node
                if start + 1 > n:
                    if new_head:
                        new_head.next = reverse_node
                    else:
                        new_head = reverse_node
                        ret = new_head
                    while new_head.next:
                        new_head = new_head.next
            else:
                node = head
                head = head.next
                if new_head:
                    new_head.next = node
                    new_head = new_head.next
                else:
                    new_head = node
                    ret = new_head
            start += 1
        return ret

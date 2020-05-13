class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        if not head.next: return head
        orig_head = self.reverseList(head.next)
        head.next = None
        return orig_head

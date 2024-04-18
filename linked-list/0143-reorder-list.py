class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # find the middle to break the list into 2 parts
        # slow will be the end of left part
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # head of right part
        curr = slow.next
        prev = None
        slow.next = None

        # reverse right part
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # merge two
        first, second = head, prev
        while second: # right part is shorter
            next1, next2 = first.next, second.next
            first.next = second
            second.next = next1
            first, second = next1, next2
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.merge2(l1, l2))
            
            lists = mergedLists
        
        return lists[0]

    def merge2(self, l1, l2):
        dummy = node = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        
        return dummy.next
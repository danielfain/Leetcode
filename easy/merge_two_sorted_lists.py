def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = ListNode(None)
        head.next = tail
        
        if not l1:
            return l2
        elif not l2:
            return l1
        
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
                
        while l1 is not None:
            tail.next = l1
            tail = tail.next
            l1 = l1.next
            
        while l2 is not None:   
            tail.next = l2
            tail = tail.next
            l2 = l2.next
            
        return head.next

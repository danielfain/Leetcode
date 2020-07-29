class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def return_kth_to_last(head, k):        # O(n) time and O(1) space
    list_len = 0
    node = head
    while node != None:
        list_len += 1
        node = node.next
    
    index = list_len - k

    for i in range(index):
        head = head.next

    return head.val


head = Node(15, Node(3, Node(11, Node(16, Node(4)))))
print(return_kth_to_last(head, 3))
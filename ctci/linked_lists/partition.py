class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def partition(head, x):         # O(n) time and O(n) space
    before_head = None
    before_tail = None
    after_head = None
    after_tail = None

    while head != None:
        if head.val < x:
            if before_head == None:
                before_head = Node(head.val)
                before_tail = before_head
            else: 
                before_tail.next = Node(head.val)
                before_tail = before_tail.next
        else:
            if after_head == None:
                after_head = Node(head.val)
                after_tail = after_head
            else: 
                after_tail.next = Node(head.val)
                after_tail = after_tail.next

        head = head.next

    before_tail.next = after_head

    return before_head


head = Node(3, Node(5, Node(2, Node(5, Node(11)))))
x = 5

result = partition(head, x)

while result != None:
    print(result.val)
    result = result.next
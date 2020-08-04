class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def delete_middle_node(node):           # O(n) time and O(n) space
    prev = node

    while node.next != None:
        prev = node
        node.val = node.next.val
        node = node.next

    prev.next = None


def delete_middle_node2(node):          # O(1) time and O(n) space
    if node == None or node.next == None:
        return False
    
    next = node.next
    node.val = next.val
    node.next = next.next


head = Node(15, Node(3, Node(11, Node(16, Node(4)))))
delete_middle_node2(head)


while head != None:
    print(head.val)
    head = head.next


# N(15) -> *N(3) -> N(11) -> N(16) -> N(4)
# N(15) -> N(11) -> N(16) -> N(4)
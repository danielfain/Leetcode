class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def remove_dupes(head):             # O(n) time and O(n) space
    hm = {}
    prev_node = Node()

    while head != None:
        if head.val in hm:
            prev_node.next = head.next
        else:
            hm[head.val] = True
            prev_node = head
        head = head.next
        

head = Node(5, Node(1, Node(3, Node(3, Node(3)))))
remove_dupes(head)

while head != None:
    print(head.val)
    head = head.next

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def palindrome(head):               # O(n) time and O(n) space
    reversed_head = reverse(head)

    while reversed_head and head:
        if reversed_head.val != head.val: return False

        reversed_head = reversed_head.next
        head = head.next

    return True


def reverse(head):
    prev = None
    current = head
    next = None

    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


head = Node("R", Node("A", Node("C", Node("E", Node("C", Node("A", Node("R")))))))
print(palindrome(head))
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def sum_lists(head1, head2):            # O(n) time and O(n) space (ITERATIVE APPROACH)
    answer_head = None
    answer_tail = None
    remainder = 0

    while head1 != None and head2 != None:
        res = head1.val + head2.val

        if res > 9:
            if answer_head == None: 
                answer_head = Node((res - 10) + remainder)
                answer_tail = answer_head
            else:
                answer_tail.next = Node((res - 10) + remainder)
                answer_tail = answer_tail.next
            remainder = 1
        else:
            if answer_head == None: 
                answer_head = Node(res + remainder)
                answer_tail = answer_head
            else:
                answer_tail.next = Node(res + remainder)
                answer_tail = answer_tail.next
            remainder = 0

        head1 = head1.next
        head2 = head2.next
    
    while head1 != None:
        answer_tail.next = Node(head1.val)
        answer_tail = answer_tail.next
        head1 = head1.next

    while head2 != None:
        answer_tail.next = Node(head2.val)
        answer_tail = answer_tail.next
        head2 = head2.next

    return answer_head


head1 = Node(2, Node(0, Node(2, Node(4))))
head2 = Node(9, Node(3, Node(3)))

result = sum_lists(head1, head2)

while result != None:
    print(result.val)
    result = result.next
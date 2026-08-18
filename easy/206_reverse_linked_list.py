def reverse_list(head):
    prev = None
    curr = head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev
class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = None
def create_linked_list(arr):
    dummy = curr = ListNode(0)
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def deleteDuplicates(head):
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


l1 = create_linked_list([1,2,2,3])
result = deleteDuplicates(l1)



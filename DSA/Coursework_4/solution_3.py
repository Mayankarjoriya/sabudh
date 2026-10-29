

class listnode:
    def __init__(self, value=0,next=None):
        self.value = value
        self.next = next

def adder(l1,l2):
    dummy = listnode(0)
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.value if l1 else 0
        val2 = l2.value if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        current.next = listnode(digit)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


def create_linked_list(arr):
    dummy = listnode(0)
    curr = dummy
    for val in arr:
        curr.next = listnode(val)
        curr = curr.next
    return dummy.next

def print_list(node):
    result = []
    while node:
        result.append(node.value)
        node = node.next
    print(result)

l1 = create_linked_list([2,4,3])
l2 = create_linked_list([5,6,4])

result = adder(l1,l2)
print_list(result)
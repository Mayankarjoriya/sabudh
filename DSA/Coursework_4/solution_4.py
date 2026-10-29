
class listnode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    dummy = curr = listnode(0)
    for val in arr:
        curr.next = listnode(val)
        curr = curr.next
    return dummy.next

def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


def merglist(lists):
    linked_list = [create_linked_list(l) for l in lists if l]
    if not linked_list:
        return None

    def mergetwopair(l1,l2):
        dummy = curr = listnode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

    def mergepair(start, end):
        if start == end:
            return linked_list[start]
        mid  = (start + end) // 2

        left = mergepair(start, mid)
        right = mergepair(mid+1, end)

        return mergetwopair(left, right)
    return mergepair(0, len(linked_list)-1)



# Using functions

input_lists = [[1,4,5],
               [1,3,4],
               [2,6]]
result = merglist(input_lists)
print_list(result)
import typing

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_llist(vals: list[typing.Any]) -> ListNode:
    """
    Takes a list of values and returns head of a linked list with
    nodes containing vals
    """
    if not vals:
        return None
    head = ListNode(vals[0])
    node = head
    for v in vals[1:]:
        node.next = ListNode(v)
        node = node.next
    return head

def get_llist_values(head: ListNode) -> list[typing.Any]:
    """
    Returns a consequtive list of values from all nodes of a linked list
    """
    res = []
    node = head
    while node:
        res.append(node.val)
        node = node.next
    return res

def print_llist(head: ListNode) -> None:
    """
    Prints nodes' values from a linked list
    """
    res = get_llist_values(head)
    print(*res)


if __name__ == '__main__':
    vls = [1,5,2,7,8,9,22]
    h = create_llist(vls)
    print_llist(h)
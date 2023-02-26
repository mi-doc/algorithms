from linked_list_tools import *
from typing import Optional


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            # The 'try' statement is convenient, because if there is no head,
            # or the list contains only one node,
            # or we reach the end of the list, and an error occures -
            # - that means there is no cycle
            slow = head
            fast = head.next

            # If 'fast' goes around a cycle and catches up with the 'slow' -
            # - there is a cycle
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


if __name__ == '__main__':
    vals = [1,3,4,2,7,7,2,4,3,1]
    head = create_llist(vals)

    node = head
    i = 3
    while node.next:
        node = node.next
        i -= 1
        if i == 0:
            target = node
    node.next = target

    sol = Solution()
    res = sol.hasCycle(head)
    print(res)

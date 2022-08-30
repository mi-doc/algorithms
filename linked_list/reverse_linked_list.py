from linked_list_tools import create_llist, print_llist, ListNode
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseListRecursive(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)

if __name__ == '__main__':
    vals = [1,3,4,2,7]
    head = create_llist(vals)

    sol = Solution()
    # res = sol.reverseListRecursive(head)
    # print_llist(res)

    from speed_tests import speed_contest
    speed_contest([
        'sol.reverseList(head)',
        'sol.reverseListRecursive(head)'
    ], globals=globals())
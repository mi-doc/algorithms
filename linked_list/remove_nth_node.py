from typing import Optional
from linked_list_tools import create_llist, print_llist, ListNode


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head

        # Pre_target is a "slow" pointer lagging n steps behind
        # so when the "fast" pointer reaches the end of the linked list,
        # the 'pre_target' pointer would stay right before the target node
        pre_target = None
        i = 1
        while node.next:
            if pre_target:
                pre_target = pre_target.next
            if i == n:
                # We've reached the gap, now let the 'slow' pointer start
                pre_target = head
            node = node.next
            i += 1

        if i == n:
            # Corner case when the target node is the head of the llist
            return head.next
        if pre_target:
            pre_target.next = pre_target.next.next

        return head

    def secondsol(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """"
        Solution from the leetcode comments
        """
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    vals = [4,3,1,2,7]
    # vals = [8,4]
    head = create_llist(vals)

    sol = Solution()
    # res = sol.removeNthFromEnd(head, 3)
    # res = sol.secondsol(head, 3)
    # print_llist(res)
    # s = Solution()


commands = [
    [ 'sol.removeNthFromEnd(head,3)'],
    [ 'sol.secondsol(head, 3)']
]

from speed_tests import speed_test

speed_test(commands, globals(), number=1)
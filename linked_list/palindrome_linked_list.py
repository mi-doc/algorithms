from linked_list_tools import *
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next

        return res == res[::-1]

    def isPalindrome2(self, head):
        # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
        rev = None
        # initially slow and fast are the same, starting from head
        slow = fast = head
        while fast and fast.next:
            # fast traverses twice as fast and moves to the end of the list if the length is odd
            # That means, when 'fast' is in the end of the list, 'slow' is in the middle
            fast = fast.next.next

            # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
        # fast is at the end, move slow one step further for comparison(cross middle one)
            slow = slow.next
        # compare the reversed first half with the second half
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        # if equivalent then rev become None, return True; otherwise return False
        return not rev


if __name__ == '__main__':
    vals = [1,3,4,2,7,7,2,4,3,1]
    head = create_llist(vals)

    sol = Solution()
    # res = sol.isPalindrome2(head)
    # print(res)

    from speed_tests import speed_contest
    speed_contest([
        'sol.isPalindrome(head)',
        'sol.isPalindrome2(head)'
    ], globals=globals())
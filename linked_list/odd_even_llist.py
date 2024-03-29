from linked_list_tools import create_llist, get_llist_values, print_llist, ListNode
from typing import Optional
from colorama import Fore, Style


class Solution:
    """
    Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
    The first node is considered odd, and the second node is even, and so on.
    Note that the relative order inside both the even and odd groups should remain as it was in the input.
    You must solve the problem in O(1) extra space complexity and O(n) time complexity.
    """

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Better solution from leetcode
        """
        if not head:
            return None

        odd, even, even_head = head, head.next, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head

def test(vals):
    sol = Solution()
    for v in vals:
        list1 = create_llist(v[0])

        head = sol.oddEvenList(list1)
        res = get_llist_values(head)

        print(
            v,
            ' -> ',
            [Fore.RED,Fore.GREEN][v[1] == res] + str(res)
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ([1,2,3,4,5], [1,3,5,2,4]),
        ([2,1,3,5,6,4,7], [2,3,6,7,1,5,4]),
        ([1], [1]),
        ([], [])
    ]

    test(vals)

from linked_list_tools import create_llist, get_llist_values, print_llist, ListNode
from typing import Optional
from colorama import Fore, Style


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, head = 0, None
        while l1 or l2 or carry:
            next_num, carry = carry, 0
            if l1:
                next_num += l1.val
                l1 = l1.next
            if l2:
                next_num += l2.val
                l2 = l2.next
            
            carry = next_num // 10
            next_num %= 10
            
            if not head:
                head = ListNode(next_num)
                node = head
            else:
                node.next = ListNode(next_num)
                node = node.next
        
        return head



def test(vals):
    sol = Solution()
    for v in vals:
        list1 = create_llist(v[0][0])
        list2 = create_llist(v[0][1])

        head = sol.addTwoNumbers(list1, list2)
        res = get_llist_values(head)

        print(
            v,
            ' -> ',
            [Fore.RED,Fore.GREEN][v[1] == res] + str(res)
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        (([2,4,3], [5,6,4]), [7,0,8]),
        (([9,9,9,9,9,9,9], [9,9,9,9]), [8,9,9,9,0,0,0,1])
    ]

    test(vals)

from platform import node
from linked_list_tools import create_llist, get_llist_values, print_llist, ListNode
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 and list2):
            return list1 or list2 or None

        # Defining the head current node of the new list
        if list1.val <= list2.val:
            head = curr = list1
            list1 = list1.next
        else:
            head = curr = list2
            list2 = list2.next

        while list1 and list2:
            if list1.val <= list2.val:
                list1, curr.next = list1.next, list1
            else:
                list2, curr.next = list2.next, list2
            curr = curr.next

        # If one list longer than another we just append it
        curr.next = list1 or list2 or None

        return head


if __name__ == '__main__':
    list1 = create_llist([1,2,4])
    list2 = create_llist([1,3,4])

    Output = [1,1,2,3,4,4]
    sol = Solution()
    res = sol.mergeTwoLists(list1, list2)

    vals = get_llist_values(res)
    print(vals == Output)
    print(vals)

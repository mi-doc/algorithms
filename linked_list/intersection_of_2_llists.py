from typing import List

# The essence of the task
TASK = """
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
"""


class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a != b:
            a = (a and a.next) or headB
            b = (b and b.next) or headA
        return a


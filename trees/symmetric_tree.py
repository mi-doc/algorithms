from fcntl import DN_DELETE
from binary_tree_tools import create_tree, TreeNode
from typing import Optional, Union


class Solution:

    def check_two_nodes_symmetry(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        '''
        Returns true if both nodes don't exist or exist and have equal values. Otherwise - False.
        '''
        if bool(node1) != bool(node2):
            return False
        if not node1 and not node2:
            return True
        if node1.val != node2.val:
            return False
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        The function compares two subtrees for symmetry
        """
        if not root or (not root.left and not root.right):
            return True

        if not self.check_two_nodes_symmetry(root.left, root.right):
            return False

        left_q = [root.left]
        right_q = [root.right]
        while left_q and right_q:
            # Two pointers - two subtrees
            left_subtr = left_q.pop(0)
            right_subtr = right_q.pop(0)

            # Check if first pair of childrean is symmetric:
            LL = left_subtr.left
            RR = right_subtr.right
            if not self.check_two_nodes_symmetry(LL, RR):
                return False
            if LL and RR:
                left_q.append(LL)
                right_q.append(RR)

            # Then check the second pair:
            LR = left_subtr.right
            RL = right_subtr.left
            if not self.check_two_nodes_symmetry(LR, RL):
                return False
            if LR and RL:
                left_q.append(LR)
                right_q.append(RL)

        # If both right and left queue are empty - subtrees are symmetrical
        return True

    def check_two_subtrees_symmetry(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """
        Recursively compares nodes for symmetry
        """
        if not self.check_two_nodes_symmetry(left, right):
            return False
        if not left:
            # If not right would work as well, as they are symmetric
            return True
        return self.check_two_subtrees_symmetry(left.right, right.left) and self.check_two_subtrees_symmetry(left.left, right.right)

    def isSymmetricRecursive(self, root: Optional[TreeNode]) -> bool:
        """
        The function compares two subtrees for symmetry recursively
        """
        if not root or (not root.left and not root.right):
            return True
        return self.check_two_subtrees_symmetry(root.left, root.right)


def test(vals):
    s = Solution()
    for val in vals:
        root = create_tree(val)
        # res = s.isSymmetricRecursive(root)
        res = s.isSymmetric(root)
        print(val, ' -> ', res)


if __name__ == '__main__':
    vals = [
        # [1,2,2,None,3,None,3],
        [5,3,3,4,5,5,4],
        [2,1,3],
        [2,1],
        [1],
        [3,4,4],
        [],
        [6,3,8,1,4,7,10,2],
        [6,3,8,1,4,7]
    ]

    test(vals)
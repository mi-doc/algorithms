import queue
from typing import Optional, Any

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(values: list[Any]) -> TreeNode:
    """
    Creates a tree from a given list of values.
    The nodes are added in breadth-first order.
    Returns the root of the new tree.
    """
    if not values:
        return None
    queue = []
    for v in values:
        if not queue:
            root = TreeNode(v)
            # If we just create TreeNodes and pass them to the queue as objects,
            # when the values list empties we would end with multiple
            # leafs with 0 as value, which we don't need
            queue.append((root, 'l'))
            queue.append((root, 'r'))
            continue

        node, node_side = queue.pop(0)
        if not v:
            # If we have None in values list, we need to take this
            # node from the queue and continue without creating a TreeNode object (skip it)
            continue
        if node_side == 'l':
            node.left = TreeNode(v)
            queue.append((node.left, 'l'))
            queue.append((node.left, 'r'))
        else:
            node.right = TreeNode(v)
            queue.append((node.right, 'l'))
            queue.append((node.right, 'r'))
    return root

def print_tree_breadth_first(root: TreeNode) -> None:
    """
    Prints values of tree nodes in breadth-first order
    """
    res = breadth_first_traversal(root)
    print(*res, end='\n')

def breadth_first_traversal(root: TreeNode) -> list[Any]:
    """
    Traverses a tree in breadth-first order. Returns a list with values.
    """
    res = []
    if not root:
        return res

    q = [root]
    while q:
        n = q.pop(0)
        res.append(n.val)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    return res

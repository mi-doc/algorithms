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
    node = TreeNode(values[0])
    root = node
    queue = [node, node]
    for v in values[1:]:
        node = queue.pop(0)
        if not node.left:
            node.left = TreeNode(v)
            queue.append(node.left)
            queue.append(node.left)
        else:
            node.right = TreeNode(v)
            queue.append(node.right)
            queue.append(node.right)

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

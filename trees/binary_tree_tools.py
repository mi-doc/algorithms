from typing import Any
from collections import deque

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

    queue = deque()
    queue.append((None, 'root'))
    for v in values:
        node, node_side = queue.popleft()
        if not v:
            # If we have None in values list, we need to take this
            # node from the queue and continue without creating a TreeNode object (skip it)
            continue
        
        n = TreeNode(v)
        match node_side:
            case 'root':
                # Corner case: defining the root
                root = n
                node = root
            case 'l':
                node.left = n
                node = node.left
            case 'r':
                node.right = n
                node = node.right

        # 'l' and 'r' stand for 'left' and 'right'
        queue.extend((node, s) for s in 'lr')

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

def level_order_traversal(root: TreeNode) -> list[Any]:
    """
    Level-order traversal. Returns a list of lists with each level nodes
    """
    res = []
    if not root:
        return res

    queue = deque()
    queue.append((root, 0))
    while queue:
        node, level = queue.popleft()

        # If we start another level, we add a new list to the res
        # to add values from this level
        if level >= len(res):
            res.append([node.val])
        else:
            res[level].append(node.val)

        queue.extend(
            (n, level + 1)
            for n in (node.left, node.right)
            if n
        )
    return res


if __name__ == '__main__':
    vals = [2,3,4,23,4123,4,5,1,1,3,3,4,4,]
    tr = create_tree(vals)
    res = level_order_traversal(tr)
    print(res)
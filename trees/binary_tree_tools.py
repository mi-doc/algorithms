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

    queue = [(None, 'root')]
    for v in values:
        node, node_side = queue.pop(0)
        if not v:
            # If we have None in values list, we need to take this
            # node from the queue and continue without creating a TreeNode object (skip it)
            continue

        if node_side == 'root':
            # Defining the root
            root = TreeNode(v)
            node = root
        elif node_side == 'l':
            node.left = TreeNode(v)
            node = node.left
        else:
            node.right = TreeNode(v)
            node = node.right

        # 'l' and 'r' stand for 'left' and 'right'
        queue.append((node, 'l'))
        queue.append((node, 'r'))

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

    queue = [(root, 0)]
    while queue:
        node, level = queue.pop(0)
        
        # If we start another level, we add a new list to the res
        # to add values from this level
        if level > len(res) - 1:
            res.append([node.val])
        else:
            res[level].append(node.val)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return res


if __name__ == '__main__':
    vals = [2,3,4,23,4123,4,5,1,1,3,3,4,4,]
    vals = [1, None, 2, None, 4, 5]
    tr = create_tree(vals)
    res = level_order_traversal(tr)
    print(res)
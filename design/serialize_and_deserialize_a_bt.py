from typing import List
from .binary_tree_tools import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            """Preorder traversal"""
            if not root:
                res.append('N')
            else:
                res.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return ','.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        self.i = 0
        def dfs():
            val = vals[self.i]
            self.i += 1
            if val == 'N':
                return None
            
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
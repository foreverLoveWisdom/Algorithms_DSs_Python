"""
* Formally, a binary tree is either empty, or a root node r together with a
    left binary tree and a right binary tree.
        - The subtrees themselves are binary trees.
        - The left binary tree is sometimes referred to as
            the left subtree of the root.
        - The right binary tree -> right subtree of the root.

* Binary tree most commonly occur in the context of binary search trees,
    wherein keys are stored in a sorted fashion.
    - At a high level, binary trees are appropriate when dealing with hierarchies.

* A node is an ancestor of d if it lies on the search path from the root to d.
    - A node is an ancestor and descendant of itself.
    - A node has no descendants except for itself is called a leaf.
    - The depth of a node is the number of nodes on the search path from the
        root to n, not including n itself.
    - The height of a binary tree is the maximum depth of a node.
    - A level of a tree is all nodes at the same depth.
"""


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

"""
- Trees: Unlike Arrays, Linked Lists, Stack and queues, which
    are linear data structures, trees are hierarchical data structures.

- The topmost node is called root of the tree.
    - The elements that are directly under an element are called
        its children.
    - The element directly above something is called its parent.

* Why?
    1. One reason to use trees might be because you want to store
        information that naturally forms a hierarchy.
            - For example, the file system on a computer.
    2. Trees (with some ordering e.g., BST) provide moderate
        access/search (quicker than Linked List and slower than arrays).
    3. Trees provide moderate insertion/deletion
        (quicker than Arrays and slower than Unordered Linked Lists).
    4. Like Linked Lists and unlike Arrays, Trees don’t have an upper limit
        on number of nodes as nodes are linked using pointers.

* Use cases:
    1. Manipulate hierarchical data.
    2. Make information easy to search (see tree traversal).
    3. Manipulate sorted lists of data.
    4. As a workflow for compositing digital images for visual effects.
    5. Router algorithms
    6. Form of a multi-stage decision-making (see business chess).

    - Main uses of trees include maintaining hierarchical data,
        providing moderate access and insert/delete operations.
            - Binary trees are special cases of tree where every node
                has at most two children.

    - Edge is the connect between 1 node to another
        - Or an edge is a line between 2 nodes.
    - Path is a sequence of nodes and edges connecting a node with a descendant.
        - When we talk about path, it includes all nodes and edges along
            the path.
        - The direction of a path is strictly from top to bottom and cannot
            be changed in the middle.
    - Height of a node is the number of edges on the longest downward
        path between that node and a leaf.
        - Every node has height.
        - Leaf can't have heights as there will be no path starting from leaf.
        
"""


# General Tree
class Tree:
    """Abstract bas class representing a tree structure."""

    # Nested position class
    class Position:
        """
        An abstraction representing the location of a single element.
        """

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """Return True if other doesn not represent the same location."""
            return not (self == other)  # opposite of __eq__

        # Abstract methods that concrete subclass must support.
        def root(self):
            """Return Position representing the tree's root (or None if empty)"""
            raise NotImplementedError("must be implemented by subclass")

        def parent(self, p):
            """Return Position representing p's parent (or None if p is root)."""
            raise NotImplementedError("must be implemented by subclass")

        def num_children(self, p):
            """Return the number of children that Position p has"""
            raise NotImplementedError("must be implemented by subclass")

        def children(self):
            """Generate an iteration of Positions representing p's children"""
            raise NotImplementedError("Must be implemented by subclass")

        def __len__(self):
            """Return the total number of elements in the tree"""
            raise NotImplementedError("must be implemented by subclass")

        # Concrete methods implemented in this class
        def is_root(self, p):
            """Return True if Position p represents the root of the tree"""
            return self.root() == p

        def is_leaf(self, p):
            """Return True if Position p does not have any children"""
            return self.num_children(p) == 0

        def is_empty(self):
            """Return True if the tree is empty."""
            return len(self) == 0

        # The depth of p is the number of ancestors of p, excluding p itself.
        def depth(self, p):
            """Return the number of levels separating Position p from the root"""
            if self.is_root(p):
                return 0
            else:
                return 1 + self.depth(self.parent(p))

        # The height of a nonempty tree T is equal to the maximum of the depths of its
        # leaf positions.
        def _height1(self):  # works, but O(n^2) worst-case time.
            """Return the height of the tree"""
            return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

        def _height2(self):  # Time is linear in size of subtree
            """Return the height of the subtree rooted at Position p."""
            if self.is_leaf():
                return 0
            else:
                return 1 + max(self._height2(c) for c in self.children(c))

        def height(self, p=None):
            """Return the height of the subtree rooted at Position p.
            If p is None, return the height of the entire tree."""
            if p is None:
                p = self.root()
            return self._height2(p)


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure"""

    # Additional abstract methods

    def lef(self, p):
        """Return a Position representing p's left child
        Return None if p does not have a left child
        """
        raise NotImplementedError("must be implemented by a subclass")

    def right(self, p):
        """Return a Position representing p's right child
        Return None if p does not have a right child
        """
        raise NotImplementedError("must be implemented by subclass")

    # Concrete methods implemented in this class
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)"""
        parent = self.parent(p)
        if parent is None:  # p must be the root
            return None  # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)  # possible None
            else:
                return self.left(parent)  # possible None

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

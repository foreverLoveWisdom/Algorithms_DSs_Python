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
        def is_root(self,):
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
                return 1 + max(self._height2(c) for c in self.children(p))

        def height(self, p=None):
            """Return the height of the subtree rooted at Position p.
            If p is None, return the height of the entire tree."""
            if p is None:
                p = self.root()
            return self._height2(p)

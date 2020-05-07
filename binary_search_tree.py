"""
* What?
    - Binary Search Tree is a node-based binary tree data structure which
        has the following properties:
        1. The left subtree of a node contains only nodes with keys
            lesser than the node’s key.
        2. The right subtree of a node contains only nodes with keys
            greater than the node’s key.
        3. The left and right subtree each must also be a binary search tree.
        4. There must be no duplicate nodes.


* When?
    - The main use case that I find relatable is in indexing database entries.

    - If you have a user table in your database with 1 million entries and
        you need to find the user with email ‘hello@world.com’,
            you can get there with a balanced binary search tree in at most
                21 iterations.

* Strengths:
    - A binary search tree does not store an index of its data elements.
        - Instead, it relies on its implicit structure
            (left or right of each node) to keep a record of where each
                element is.
                    - The result is insertion and deletion at logarithmic time,
                        or O(log n).

    - Because of this structure, insertion and deletion of nodes can be
        achieved very quickly.
        - Instead of traversing every element sequentially until
            the right one is found, which is how we work with arrays,
                we only need to traverse half the tree, then
                    half of half the tree, then half of half of
                        half the tree… I think you get the picture –
                            the result is much faster
                                insertion/deletion than array,
                                    with almost none of the draw backs.

    - BST can search, access, insert, and delete data elements in
        logarithmic time O(log n)

* Weaknesses:
    - A binary search tree can get out of balance.
        - This is the first thing to realise about a binary search tree.

    - Ugliness is not the only problem with such a tree – performance,
        as you can imagine, will also be negatively affected.
        - For example, to search such a tree, we would have to
            traverse practically all the nodes in sequence.
                - In this situation, which is really the worst case scenario
                    of a binary search tree, we might as well be using
                        a conventional array!

    - It’s interesting – some refer to a horribly imbalanced tree as
        a “degenerate.”
            - The more imbalanced, the more degenerate it is,
                and the closer it is to behaving like an array.

    - BST is slightly slower than an array at access (O(log n) vs O(1))
"""

"""
* Binary search tree is a workhorse of data structures and can be used to
solve almost every data structures problem reasonably efficiently.

* They offer the ability to efficiently search for a key as well as find
    the min and max element.

* BST is similar to array in that the stored values (the keys) are stored
in a sorted order.
    - Unlike with a sorted array, keys can be added to and deleted from
        a BST efficiently


* A common mistake with BST is that an object that is present in a BST
    - is not updated. The consequence is that a lookup for that object
        returns false, even though it's still in the BST.

* As a rule, avoid putting mutable objects in a BST. Otherwise, when
    a mutable object that is in a BST is to be updated,
        always first remove it from the tree, then update it, then add it back.
"""


"""
* Searching is the single most fundamental application of BSTs.
    Unlike a hash table, a BST offers the ability to find the min
        and max elements, and find the next largest/next smallest element.

    - These operations, along with lookup, delete, and find, take time O(lgn)
        for library implementations of BST.

    - Both BST and hash table use O(n) space. In practice,
        BST will use slightly more.
"""


class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

    def search_bst(self, tree, key):
        return (
            tree
            if not tree or tree.data == key
            else self.search_bst(tree.left, key)
            if key < tree.data
            else self.search_bst(tree.right, key)
        )

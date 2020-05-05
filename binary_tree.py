"""
* What?
    - A tree whose elements have at most 2 children is called
        a binary tree.
            - Since each element in a binary tree can have
                only 2 children, we typically name them
                    the left and right child.
    
    - A Binary Tree node contains following parts.
        1. Data
        2. Pointer to left child
        3. Pointer to right child

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
"""

# A Python class that represents an individual node
# In a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(vars(root))

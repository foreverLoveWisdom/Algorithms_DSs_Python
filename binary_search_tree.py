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
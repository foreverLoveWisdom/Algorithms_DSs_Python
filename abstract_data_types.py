"""
1. What is data type?
    - A data type is a way of telling the compiler or machine,
        about what valid values a particular variable can hold.
        - E.g, int a = 1;
            => This var can only hold integral values.
                => Throws an error if assign it with a boolean value.
    
    - A data type is a concrete concept.
    
2. An ADT(abstract data type), is simply a mathematical model.
    - It is a way of logically stating a mathematical concept or
        data structure. 
        - It may or may not be fully implemented.
        - It is up to the programmer to define the implementation for ADTs or
            to import them from other headers or libraries.
    
    - A mathematical model is a description of a system using
        mathematical concepts and language.
        => A model may help to explain a system and to study the effects
            of different components, and to make 
                predictions about behaviour.  
    
    - The key thing to notice here is that, we are not concerned how
        the stack is implemented or represented internally.
        - We are only concerned with what operations the stack supports,
            namely Push(), Pop(), and Top().
    
    - So, the key difference is that, while a data type represents encapsulation,
        an ADT represents abstraction.
        - An abstract data type (ADT) is a specification for how an ‘data’
            interface should behave without any reference
                to its actual implementation.
"""

"""
* ADT:
    1. Stack
    2. Queue
    3. Bag
    4. List
    5. Priority Queue
    6. Trie
    7. Heap
    8. Binary Tree
    9. Set
    10. Map
    
* Data structures:
    1. array
    2. linked list
    3. hash map/dictionary
"""
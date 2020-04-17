"""
The worst way to live is to think small, and act small.

List problems have a simple brute-force solution that uses O(n) space, but
a subtler solution that uses the existing list nodes to
reduce space complexity to O(1)

Very often, a problem on lists is conceptually simple, and is
more about cleanly coding what's specified, rather than
designing an algorithm

Consider using a dummy head (sometimes referred to as a sentinel) to
avoid having to check for empty lists.
This simplifies code,and makes bugs less likely.

It's easy to forget to update the next (and previous for double linked list)
for the head and tail.

Algorithms operating on singly linked lists often benefit from
using 2 iterators, one ahead of the other, or
one advancing quicker than the other.
"""


class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    @staticmethod
    def search_list(L, key):
        while L and L.data != key:
            L = L.next

        # If key was not present in the list, L will have become null.
        return L

    @staticmethod
    def insert_after(node, new_node):
        new_node.next = node.next
        node.next = new_node

    @staticmethod
    def delete_after(node):
        node.next = node.next.next

    @staticmethod
    def merge_2_lists(l1, l2):
        dummy_head = tail = ListNode()
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Append the remaining nodes of l1 or l2
        tail.next = l1 or l2
        return dummy_head.next

    @staticmethod
    def traverse_link_list(node):
        while node:
            print(node.data)
            node = node.next


# node1 = ListNode(1)
# node2 = ListNode(3)
# ListNode.insert_after(node1, node2)

# node3 = ListNode(2)
# node4 = ListNode(4)
# ListNode.insert_after(node3, node4)

# node5 = ListNode.merge_2_lists(node1, node3)
# ListNode.traverse_link_list(node5)

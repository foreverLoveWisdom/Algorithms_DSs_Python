import link_list


# def print_linked_list_in_reverse(head):
#     nodes = []
#     while head:
#         nodes.append(head.data)
#         head = head.next
#     while nodes:
#         print(nodes.pop())


# node1 = link_list.ListNode()
# node2 = link_list.ListNode(1)
# node3 = link_list.ListNode(2)
# link_list.ListNode().insert_after(node1, node2)
# link_list.ListNode().insert_after(node2, node3)
# print_linked_list_in_reverse(node1)

class Stack():
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        self.data.pop()

    def max_ele(self):
        # stk = self.data.copy()
        # stk.sort()
        # return stk[-1]
        max_num = 0
        for i in self.data:
            if i > max_num:
                max_num = i

        return max_num


stk = Stack()
stk.push(2)
stk.push(1)
stk.push(5)
stk.push(-10)

print(stk.max_ele())
print(stk.data)
